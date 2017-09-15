/* -*-mode:c++; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2 -*- */

#ifndef REMOTE_HH
#define REMOTE_HH

#include <sys/types.h>
#include <string>
#include <unordered_map>

#include "thunk.hh"
#include "lambda.hh"
#include "http_request.hh"
#include "http_response_parser.hh"
#include "aws.hh"
#include "secure_socket.hh"
#include "address.hh"

class RemoteResponse
{
private:
  RemoteResponse();

public:
  enum class Type
  {
    SUCCESS,
    EXECUTION_FAILURE,
    LAMBDA_FAILURE,
    RATE_LIMIT
  } type;

  std::string thunk_hash;
  std::string output_hash;
  off_t output_size;
  bool is_executable;

  static RemoteResponse parse_message( const std::string & message );
};

namespace lambda {

  class RequestGenerator
  {
  private:
    AWSCredentials credentials_;
    std::string region_;

  public:
    RequestGenerator( const AWSCredentials & credentials, const std::string & region );
    HTTPRequest generate( const gg::thunk::Thunk & thunk, const std::string & thunk_hash,
                          const bool timelog = true );
  };

  struct ConnectionContext
  {
    enum class State { needs_connect, needs_ssl_read_to_connect, needs_ssl_write_to_connect, ready };

    State state { State::needs_connect };

    SecureSocket socket;
    HTTPResponseParser responses {};
    HTTPRequest request {};

    ConnectionContext( SecureSocket && sock, HTTPRequest && request )
      : socket( std::move( sock ) ), request( std::move ( request ) ) {}
    bool ready() const { return state == State::ready; }

    void continue_SSL_connect();
  };

  class ExecutionConnectionManager
  {
  private:
    SSLContext ssl_context_ {};
    Address address_;
    RequestGenerator request_generator_;

    /* thunk_hash -> socket */
    std::unordered_map<std::string, ConnectionContext> connections_ {};

  public:
    ExecutionConnectionManager( const AWSCredentials & credentials,
                                const std::string & region );
    ConnectionContext & new_connection( const gg::thunk::Thunk & thunk,
                                        const std::string & hash );
    void remove_connection( const std::string & hash );
  };

}

#endif /* REMOTE_HH */

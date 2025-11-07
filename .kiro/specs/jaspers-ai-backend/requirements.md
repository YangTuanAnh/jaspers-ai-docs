# Requirements Document

## Introduction

Jaspers AI is a financial portfolio management and AI-powered advisory platform that aggregates data from multiple brokerage accounts (Alpaca and Interactive Brokers), provides real-time portfolio analytics, and offers conversational AI assistance powered by Claude. The backend system must securely manage user authentication, integrate with external brokerage and financial data APIs, maintain portfolio state, and provide intelligent chat capabilities with retrieval-augmented generation (RAG).

## Glossary

- **Backend System**: The NestJS-based server application that handles all API requests, business logic, and data persistence
- **User**: An authenticated individual who connects brokerage accounts and interacts with the platform
- **Brokerage Connection**: An authenticated link between a User's account and an external brokerage provider (Alpaca or IBKR)
- **Portfolio**: The aggregated collection of all holdings across a User's connected Brokerage Connections
- **Holding**: A specific position in a security (stock) with quantity, cost basis, and current market value
- **Chat Session**: A conversation thread between a User and the AI assistant
- **RAG Pipeline**: Retrieval-Augmented Generation system that fetches relevant data before generating AI responses
- **Citation**: A reference to a data source used in an AI response
- **JWT**: JSON Web Token used for stateless authentication
- **OAuth**: Open Authorization protocol for secure third-party authentication
- **EDGAR**: SEC's Electronic Data Gathering, Analysis, and Retrieval system for company filings

## Requirements

### Requirement 1

**User Story:** As a new user, I want to register for an account with my email and password, so that I can securely access the platform

#### Acceptance Criteria

1. WHEN a User submits registration data with valid email and password, THE Backend System SHALL create a new user record with bcrypt-hashed password
2. WHEN a User submits registration data with a password shorter than 8 characters, THE Backend System SHALL reject the request with a validation error
3. WHEN a User submits registration data with an email already in use, THE Backend System SHALL reject the request with a conflict error
4. THE Backend System SHALL require passwords to contain at least one uppercase letter, one lowercase letter, and one number
5. WHEN a User successfully registers, THE Backend System SHALL return a JWT access token valid for 15 minutes and a refresh token valid for 7 days

### Requirement 2

**User Story:** As a registered user, I want to log in with my credentials, so that I can access my portfolio and chat history

#### Acceptance Criteria

1. WHEN a User submits valid email and password credentials, THE Backend System SHALL authenticate the User and return JWT tokens
2. WHEN a User submits invalid credentials, THE Backend System SHALL reject the request and increment the failed login counter
3. WHEN a User attempts login more than 5 times within 15 minutes from the same IP address, THE Backend System SHALL block further attempts with rate limit error
4. WHEN a User successfully logs in, THE Backend System SHALL create an audit log entry with timestamp, IP address, and user agent
5. THE Backend System SHALL verify password using bcrypt comparison with stored hash

### Requirement 3

**User Story:** As an authenticated user, I want to connect my Alpaca brokerage account, so that my portfolio data can be synced automatically

#### Acceptance Criteria

1. WHEN a User initiates Alpaca connection, THE Backend System SHALL generate an OAuth authorization URL with PKCE parameters
2. WHEN Alpaca redirects to the callback endpoint with authorization code, THE Backend System SHALL exchange the code for access and refresh tokens
3. WHEN the Backend System receives brokerage tokens, THE Backend System SHALL encrypt tokens using AES-256 before storing in database
4. WHEN a Brokerage Connection is established, THE Backend System SHALL create an audit log entry recording the connection event
5. THE Backend System SHALL store the external account ID from Alpaca for future reconciliation

### Requirement 4

**User Story:** As an authenticated user, I want to connect my Interactive Brokers account, so that I can aggregate holdings from multiple brokerages

#### Acceptance Criteria

1. WHEN a User submits IBKR credentials, THE Backend System SHALL authenticate with IBKR Client Portal API and establish a session
2. WHEN an IBKR session is established, THE Backend System SHALL encrypt session tokens using AES-256 before storing
3. WHEN an IBKR connection health check fails, THE Backend System SHALL mark the connection status as error
4. THE Backend System SHALL execute IBKR session tickle requests every 5 minutes to maintain active connection
5. WHEN a User disconnects a Brokerage Connection, THE Backend System SHALL delete encrypted tokens and create an audit log entry

### Requirement 5

**User Story:** As a user with connected brokerages, I want my portfolio to sync automatically, so that I always see current holdings and values

#### Acceptance Criteria

1. THE Backend System SHALL execute portfolio sync operations every 15 minutes during market hours (9:30 AM - 4 PM ET)
2. WHEN a portfolio sync executes, THE Backend System SHALL fetch positions from all connected Brokerage Connections
3. WHEN multiple Brokerage Connections hold the same symbol, THE Backend System SHALL aggregate quantities and calculate weighted average cost
4. WHEN one Brokerage Connection fails during sync, THE Backend System SHALL continue syncing other connections and return partial results
5. WHEN portfolio sync completes, THE Backend System SHALL update the last_synced timestamp for each Holding

### Requirement 6

**User Story:** As a user, I want to view my portfolio summary with total value and P&L, so that I can understand my overall investment performance

#### Acceptance Criteria

1. WHEN a User requests portfolio summary, THE Backend System SHALL calculate total market value as sum of all Holdings' current values
2. WHEN calculating unrealized P&L, THE Backend System SHALL compute (current_price - average_cost) \* quantity for each Holding
3. WHEN calculating P&L percentage, THE Backend System SHALL compute (unrealized_pl / cost_basis) \* 100
4. THE Backend System SHALL cache portfolio summary data with 30-second TTL to reduce database load
5. WHEN a User requests portfolio summary, THE Backend System SHALL return data within 500 milliseconds

### Requirement 7

**User Story:** As a user, I want to retrieve real-time stock quotes, so that I can see current market prices for my holdings

#### Acceptance Criteria

1. WHEN a User requests a stock quote during market hours, THE Backend System SHALL fetch data from Yahoo Finance API
2. WHEN Yahoo Finance API fails, THE Backend System SHALL attempt to fetch quote from Finnhub API as fallback
3. THE Backend System SHALL cache stock quotes with 1-minute TTL during market hours (9:30 AM - 4 PM ET)
4. THE Backend System SHALL cache stock quotes with 1-hour TTL outside market hours
5. WHEN both Yahoo Finance and Finnhub APIs fail, THE Backend System SHALL return cached data if available

### Requirement 8

**User Story:** As a user, I want to search SEC EDGAR filings for companies, so that I can research fundamental information

#### Acceptance Criteria

1. WHEN a User searches filings by ticker symbol, THE Backend System SHALL query SEC EDGAR API with the corresponding CIK
2. WHEN the Backend System retrieves EDGAR filings, THE Backend System SHALL cache filing data indefinitely as filings are immutable
3. THE Backend System SHALL limit EDGAR API requests to 10 requests per second to comply with SEC rate limits
4. WHEN a User requests a specific filing by accession number, THE Backend System SHALL retrieve and parse the filing content
5. THE Backend System SHALL log all EDGAR API calls to api_usage_logs table for monitoring

### Requirement 9

**User Story:** As a user, I want to create a chat session and ask questions about my portfolio, so that I can get AI-powered insights

#### Acceptance Criteria

1. WHEN a User creates a chat session, THE Backend System SHALL generate a unique session ID and store it with user association
2. WHEN a User sends a message, THE Backend System SHALL parse the message to extract ticker symbols and time ranges
3. WHEN the RAG Pipeline processes a query, THE Backend System SHALL fetch relevant Portfolio data from database
4. WHEN the RAG Pipeline identifies mentioned symbols, THE Backend System SHALL retrieve current stock quotes for those symbols
5. THE Backend System SHALL include the last 10 messages from the Chat Session as conversation context

### Requirement 10

**User Story:** As a user, I want AI responses to include citations, so that I can verify the sources of information

#### Acceptance Criteria

1. WHEN the Backend System generates an AI response, THE Backend System SHALL track all data sources used during RAG Pipeline execution
2. WHEN a data source is used, THE Backend System SHALL format a citation with source name, data type, and timestamp
3. THE Backend System SHALL store citations in the chat_messages.citations_json field as a JSON array
4. WHEN Yahoo Finance provides quote data, THE Backend System SHALL create a citation formatted as "[Source: Yahoo Finance - {SYMBOL} Quote, {DATE}]"
5. WHEN SEC EDGAR provides filing data, THE Backend System SHALL create a citation with filing type, quarter, and document URL

### Requirement 11

**User Story:** As a user, I want the AI to use tools to fetch real-time data, so that responses are based on current information

#### Acceptance Criteria

1. WHEN Claude API requests tool execution, THE Backend System SHALL execute the requested tool server-side
2. THE Backend System SHALL define tools including get_portfolio_holdings, get_stock_quote, search_company_news, and search_edgar_filings
3. WHEN a tool executes, THE Backend System SHALL return structured data to Claude API for synthesis
4. WHEN a tool execution fails, THE Backend System SHALL return an error message to Claude API allowing graceful degradation
5. THE Backend System SHALL log tool execution time and success status for monitoring

### Requirement 12

**User Story:** As a user, I want my authentication tokens to refresh automatically, so that I don't get logged out during active sessions

#### Acceptance Criteria

1. WHEN a User's access token expires, THE Backend System SHALL accept a valid refresh token to issue a new access token
2. WHEN a User changes their password, THE Backend System SHALL invalidate all existing refresh tokens
3. THE Backend System SHALL issue access tokens with 15-minute expiration
4. THE Backend System SHALL issue refresh tokens with 7-day expiration
5. WHEN a refresh token is used, THE Backend System SHALL rotate the refresh token and return a new one

### Requirement 13

**User Story:** As a user, I want my brokerage tokens to refresh automatically, so that my portfolio stays synced without manual reconnection

#### Acceptance Criteria

1. WHEN an Alpaca access token expires within 5 minutes, THE Backend System SHALL use the refresh token to obtain new tokens
2. WHEN token refresh succeeds, THE Backend System SHALL encrypt and store the new tokens
3. WHEN token refresh fails, THE Backend System SHALL mark the Brokerage Connection status as error
4. THE Backend System SHALL check Brokerage Connection health every 5 minutes
5. WHEN a Brokerage Connection health check detects invalid tokens, THE Backend System SHALL attempt automatic token refresh

### Requirement 14

**User Story:** As a user, I want my portfolio performance tracked over time, so that I can see historical trends

#### Acceptance Criteria

1. THE Backend System SHALL create a daily portfolio snapshot at 4:00 PM ET when market closes
2. WHEN creating a snapshot, THE Backend System SHALL record total portfolio value, cash balance, and total P&L
3. WHEN a User requests performance data, THE Backend System SHALL retrieve snapshots for the requested time range
4. THE Backend System SHALL calculate day-over-day, week-over-week, and month-over-month performance percentages
5. WHEN insufficient historical data exists, THE Backend System SHALL return available data without error

### Requirement 15

**User Story:** As a user, I want the system to handle API failures gracefully, so that I still receive partial data when possible

#### Acceptance Criteria

1. WHEN an external API request times out after 10 seconds, THE Backend System SHALL log the timeout and return cached data if available
2. WHEN Finnhub API rate limit is reached, THE Backend System SHALL queue requests and retry after rate limit window expires
3. WHEN a Brokerage Connection API fails during portfolio sync, THE Backend System SHALL continue syncing other connections
4. THE Backend System SHALL implement exponential backoff with maximum 3 retry attempts for failed API calls
5. WHEN all data sources fail and no cache exists, THE Backend System SHALL return an error response with status code 503

### Requirement 16

**User Story:** As a platform administrator, I want security audit logs for all authentication events, so that I can detect suspicious activity

#### Acceptance Criteria

1. WHEN a User logs in successfully, THE Backend System SHALL create an audit log with timestamp, user ID, IP address, and user agent
2. WHEN a User login fails, THE Backend System SHALL create an audit log with attempted email and IP address
3. WHEN a User changes their password, THE Backend System SHALL create an audit log entry
4. WHEN a Brokerage Connection is created or deleted, THE Backend System SHALL create an audit log entry
5. THE Backend System SHALL retain audit logs for minimum 90 days

### Requirement 17

**User Story:** As a user, I want API rate limiting to protect the platform, so that the service remains available during high traffic

#### Acceptance Criteria

1. THE Backend System SHALL limit authenticated users to 1000 requests per hour
2. THE Backend System SHALL limit login attempts to 5 per 15 minutes per IP address
3. THE Backend System SHALL limit chat message submissions to 10 per minute per session
4. THE Backend System SHALL limit manual portfolio sync requests to 4 per hour per user
5. WHEN rate limit is exceeded, THE Backend System SHALL return HTTP 429 status with X-RateLimit-Reset header

### Requirement 18

**User Story:** As a user, I want my sensitive data encrypted, so that my brokerage credentials are protected

#### Acceptance Criteria

1. THE Backend System SHALL encrypt all brokerage access tokens using AES-256 encryption before database storage
2. THE Backend System SHALL encrypt all brokerage refresh tokens using AES-256 encryption before database storage
3. THE Backend System SHALL store encryption keys in environment variables separate from database
4. THE Backend System SHALL hash all passwords using bcrypt with minimum 10 salt rounds
5. THE Backend System SHALL transmit all data over HTTPS in production environment

### Requirement 19

**User Story:** As a user, I want the system to normalize data from different providers, so that I receive consistent response formats

#### Acceptance Criteria

1. WHEN the Backend System fetches quotes from Yahoo Finance, THE Backend System SHALL transform response to standard quote format
2. WHEN the Backend System fetches quotes from Finnhub, THE Backend System SHALL transform response to standard quote format
3. THE Backend System SHALL ensure all stock quote responses include symbol, price, change, change_percent, and timestamp fields
4. WHEN the Backend System aggregates holdings from multiple brokerages, THE Backend System SHALL normalize position data to common schema
5. THE Backend System SHALL convert all timestamps to UTC before storage

### Requirement 20

**User Story:** As a user, I want the chat interface to track token usage, so that the platform can monitor costs

#### Acceptance Criteria

1. WHEN Claude API returns a response, THE Backend System SHALL extract input token count and output token count
2. THE Backend System SHALL store token counts in chat_messages table for each message
3. THE Backend System SHALL calculate estimated cost using $3 per 1M input tokens and $15 per 1M output tokens
4. WHEN a User requests usage analytics, THE Backend System SHALL aggregate token usage across all Chat Sessions
5. THE Backend System SHALL log processing time in milliseconds for each AI response

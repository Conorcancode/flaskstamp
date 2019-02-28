# FlaskStamp - A Flask Based Timestamp Microservice

## How it Works

1.  The API endpoint is requested at the url + `/api/timestamp/`
2.  Upon request, the server will return the current date in UNIX and UTC format as JSON data. NOTE: UTC timestamp is in the GMT timezone.
3.  An UNIX or UTC timestamp can be appended to the URL to have the server return the UNIX and UTC timestamps at that time. URL + `/api/timestamp/2011-04-15` UTC must use dashes: `-` to separate year, month and day.



## Examples

1.  Base URL + `/api/timestamp/`
returns
`{"timestamps":{"unix":1551365650.0436215,"utc":"Thu, 28 Feb 2019 14:54:10 GMT"}}` [View](https://mighty-wave-38268.herokuapp.com/api/timestamp/)

2.  Base URL + `/api/timestamp/2011-04-15` 
returns 
`{"timestamps":{"unix":1302825600.0,"utc":"Fri, 15 Apr 2011 00:00:00 GMT"}}` [View](https://mighty-wave-38268.herokuapp.com/api/timestamp/2011-04-15)

3.  Base URL + `/api/timestamp/1489093749`
returns
`{"timestamps":{"unix":1489093749,"utc":"Thu, 09 Mar 2017 21:09:09 GMT"}}` [View](https://mighty-wave-38268.herokuapp.com/api/timestamp/2011-04-15)

</section>

<section id="errors">

## Errors

If there is an error, the server will return `{"timestamps":{"Error":"Invalid Date"}}`. The following are common errors that could have been made.

*   There is not a full YYYY/MM/DD indicated in the request e.g. BASE URL + `/api/timestamp/31-3`
*   There are more than 10 digits in the request e.g. BASE URL + `/api/timestamp/85938493201`
*   The request is neither a string of digits nor a valid UTC timestamp. It may have a character other than "`-`" in the request.
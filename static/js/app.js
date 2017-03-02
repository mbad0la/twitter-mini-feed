/* when document has finished loading */
$(function() {

  /* make AJAX request to `/api/custserv` */
  $.ajax({
    url: '/api/custserv',
    dataType: 'json',
    type: 'get',
    success: function(response) {

      /* map every tweet object to it's HTML template */
      /* then concatenate all elements in the array */
      response = response
      .map(tweet => (
        `<div class="tweet">
          <div class="container">
            <div class="tweet-head">
              <div class="tweet-user-img">
                <img src="${tweet.user.profile_image_url_https}">
              </div>
              <div class="tweet-user-meta">
                <div><b>${tweet.user.name}</b></div>
                <div class="handle">@${tweet.user.screen_name}</div>
              </div>
            </div>
            <div class="tweet-body">
              ${tweet.text}
            </div>
            <div class="tweet-footer">
              <span class="favourites"><i class="fa fa-heart" aria-hidden="true"></i> ${tweet.user.favourites_count}</span>
              <span class="retweets"><i class="fa fa-retweet" aria-hidden="true"></i> ${tweet.retweet_count}</span>
              <span class="created-at">${tweet.created_at}</span>
            </div>
          </div>
        </div>`
      ))
      .join('')

      /* inject into DOM */
      $('#tweets').css('text-align', 'initial').empty().append(response)

    },
    error: function(error) {
      console.log(error)
    }
  })

})

# Import necessary libraries
from bs4 import BeautifulSoup

# Sample HTML content (as provided)
html_content = """
<!DOCTYPE tml>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="user-scalable=no,initial-scale=1,maximum-scale=1,minimum-scale=1,width=device-width,viewport-fit=cover" name="viewport"/>
<style>
... (style content omitted for brevity) ...
</style>
<title id="browser-title">
 iGP Manager
</title>
<link href="/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png"/>
<link href="/site.webmanifest" rel="manifest"/>
<script>
... (script content omitted for brevity) ...
</script>
<body class="preload" dir="ltr" id="body">
 <noscript class="error">
  This website requires JavaScript, but it is disabled in your browser. Enable JavaScript to continue.
 </noscript>
 <noscript>
  <img height="1" src="https://www.facebook.com/tr?id=2418348511527380&amp;ev=PageView&amp;noscript=1" style="display:none" width="1"/>
 </noscript>
 <div id="curtain">
 </div>
 <div id="textCheck" style="display:none;padding:0;margin:0;box-sizing:border-box;border:none;line-height:1!important">
  TEST
 </div>
 <div id="myProfileContainer" style="display:none">
  <div class="container">
   <div id="myProfile">
    <div id="myProfileAccount">
     <a class="closeDialog btn" href="p=manager" id="mManager">
      <span class="left" id="myProfilePic">
      </span>
      <span class="robotoBold nowrap" id="myProfileName">
       {11}
      </span>
      <br/>
      <span class="nowrap" id="myProfileTeam">
       {10}
      </span>
     </a>
    </div>
    <a href="d=shortlist" id="nShortlistHome">
     <icon>
      md-clipboard
     </icon>
     <span id="myProfileShortlist">
     </span>
    </a>
    <a href="d=notes">
     <icon>
      md-document
     </icon>
     <span id="myProfileNotes">
     </span>
    </a>
    <div id="menu-footer">
     <a class="closeDialog tooltip" data-tip="{16}" href="p=settings" id="mSettings">
      <icon>
       md-settings
      </icon>
     </a>
     <a class="closeDialog tooltip" data-tip="{17}" href="p=help" id="mHelp">
      <icon>
       md-help-circle
      </icon>
     </a>
     <a class="confirm" data-tip="&lt;p&gt;{19}&lt;/p&gt;&lt;div class='two-btn'&gt;&lt;a href='type=logout&amp;jsReply=logout&amp;ajax=1' class='btn'&gt;&lt;icon&gt;checkmark&lt;/icon&gt;&lt;/a&gt;&lt;a href='#' class='btn3 close'&gt;&lt;icon&gt;cancel&lt;/icon&gt;&lt;/a&gt;&lt;/div&gt;" href="#" id="mLogout">
      <icon>
       md-log-out
      </icon>
     </a>
    </div>
   </div>
  </div>
 </div>
 <div id="tutorial-container">
 </div>
 <noscript>
  <img height="1" src="https://www.facebook.com/tr?id=308363319356454&amp;ev=PageView&amp;noscript=1" style="display:none" width="1"/>
 </noscript>
 <div id="loader">
  <div id="loader-bg">
   <div id="load8">
   </div>
   <div id="loader-icon">
   </div>
  </div>
  <div class="pulsate" id="loader-text" style="display:none">
   Loading...
  </div>
 </div>
 <div id="fb-root">
 </div>
 <div id="header">
  <div class="container">
   <div id="head-l">
    <a class="menuHidden" href="#" id="menu-toggle">
     <img alt="iGP" src="https://static.igpmanager.com/igp/design/image/logo.png"/>
    </a>
   </div>
   <div id="head-c">
    <h1 id="page-title">
     iGP Manager
    </h1>
   </div>
   <div id="head-r">
    <a class="robotoBold" href="d=invest" id="balance">
     <span id="balanceText">
     </span>
     <div class="trPlus">
      <icon>
       add
      </icon>
     </div>
    </a>
    <a class="robotoBold" href="d=tokens" id="tokens">
     <img alt="T" class="icon-16" src="https://static.igpmanager.com/igp/design/icon/token-32.png"/>
     <span id="tokens-total">
      -
     </span>
     <div class="trPlus">
      <icon>
       add
      </icon>
     </div>
    </a>
    <div id="historyBtns">
     <a class="disabled" href="#" id="back">
      <icon>
       ios-arrow-back
      </icon>
     </a>
     <a class="disabled" href="#" id="forward">
      <icon>
       ios-arrow-forward
      </icon>
     </a>
    </div>
    <div class="pointer" id="headerProfile">
    </div>
    <a class="disabled" href="#" id="action">
     ...
    </a>
   </div>
   <div class="clear">
   </div>
  </div>
 </div>
 <div class="clear">
 </div>
 <div id="modal-wrap">
  <div id="dialog-wrap">
   <div class="container" id="dialogs-container">
   </div>
  </div>
  <div id="tutorial-wrap">
  </div>
 </div>
 <div class="container" id="page-content">
  <div id="page-head">
   <h1>Page Title</h1>
  </div>
  <div class="news">
   <h2>Latest News</h2>
   <img src="news_image.jpg" alt="News Image">
   <span class="date">Date: 2024-05-26</span>
   <p>News content goes here. This is a sample news content.</p>
  </div>
 </div>
</body>
"""


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the title of the webpage
page_title = soup.title.string if soup.title else 'No Title Found'

# Example of extracting meta information (like viewport content)
meta_viewport = soup.find('meta', attrs={'name': 'viewport'})
viewport_content = meta_viewport['content'] if meta_viewport else 'No viewport meta tag found'

# Print extracted information
print(f"Page Title: {page_title}")
print(f"Viewport Content: {viewport_content}")

# You can add more extraction logic as needed

# The output will be printed to the console

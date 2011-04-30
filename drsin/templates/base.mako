<html>
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<meta name="google-site-verification" content="PK9dkrkE3iMUwE8l8B2akGIs4ZG82OXiBI5qyCMD2fw" />
		<title>Dr SinJax entertains Magical Thoughts</title>
		
		
		
		<script type="text/javascript" src="/js/syntaxhighlighter/shCore.js"></script>
		<script type="text/javascript" src="/js/syntaxhighlighter/shBrushJScript.js"></script>
		<script type="text/javascript" src="/js/syntaxhighlighter/shBrushPython.js"></script>
		<script type="text/javascript" src="/js/syntaxhighlighter/shBrushBash.js"></script>
		<script type="text/javascript" src="/js/syntaxhighlighter/shBrushJava.js"></script>
		<script type="text/javascript" src="/js/syntaxhighlighter/shBrushGroovy.js"></script>
		<script type="text/javascript" src="/js/syntaxhighlighter/shBrushXml.js"></script>
		<script type="text/javascript" src="/js/syntaxhighlighter/shBrushCss.js"></script>
		<script type="text/javascript" src="/js/syntaxhighlighter/shBrushPlain.js"></script>
		
		

		
		<!-- <link rel="stylesheet" href="/css/autocomplete/demo/main.css" type="text/css" /> -->
		<link rel="stylesheet" href="/css/autocomplete/jquery.autocomplete.css" type="text/css" />
		<link href="/css/syntaxhighlighter/shCore.css" rel="stylesheet" type="text/css" />
		<link type="text/css" rel="Stylesheet" href="/css/syntaxhighlighter/shThemeDjango.css"/>
		<link type="text/css" rel="stylesheet" href="${h.url_for(controller='style')}"/> 
		<link href="${h.url_for(controller='post',action='rss')}" rel="alternate" type="application/rss+xml" title="MagicalThinking" />
		<script src="/js/jquery-1.4.2.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript" src="/js/autocomplete/lib/jquery.bgiframe.min.js"></script>
		<script type="text/javascript" src="/js/autocomplete/lib/jquery.dimensions.js"></script>
		<script type="text/javascript" src="/js/autocomplete/jquery.autocomplete.js"></script>
		<script type="text/javascript" charset="utf-8">
			$(document).ready(function () {
				$.get('${h.url_for(controller="style",action="recentPubs")}', function(data) {
				  $('#recentPubs').html(data);
				});
				$("pre").each(function (thing,actual) {
					if($(actual).attr("class") == "")
					{
						$(actual).attr("class","brush: bash")
					}
				})
				SyntaxHighlighter.all()
			})
		</script>
		%if next!=None and hasattr(next,"head"):
			${next.head()}
		%endif
	</head>
	<body>
		<div id="topbar">
			<p>Sina Samangooei's thoughts. Musings of an engineer trapped in an academic's body.
			% if "user" in session and session["user"]:
			<a href="${h.url_for('/logout')}"> logout </a>
			% else:
			<a href="${h.url_for('/login')}"> login </a>
			% endif
			</p>
		</div>
		<%
		flash = h.getFlash()
		%>
		% if flash:
		<div id="flash">
		<%
		errors = flash.get("error",[])
		messages = flash.get("message",[])
		%>

		<ul class="errors">
		% for error in errors:
		<li>${error}</li>
		% endfor
		</ul>
		<ul class="messages">
		% for message in messages:
		<li>${message}</li>
		% endfor
		</ul>
		</div>
		<div class="clearer">

		</div>
		%endif
		<div id="holder">
			<h1 id="magical_thinking"><a href="${h.url_for('/')}">Magical<strong>Thinking</strong>.</a></h1>
			<div id="content" class="structure">
				<div class="header">
					<h3><strong>I have</strong> <em>something to add...</em></h3>
				</div>
				${next.body()}
			</div>
			<div id="menu" class="structure">
				<div class="structure">
					<h3><strong>with</strong> <em> plenty of ego...</em></h3>
					<img src="${h.url_for(controller='style',action='face')}"/>
					<p>
						<%
						import datetime
						now = datetime.datetime.now()
						birthday=4.0/12.0
						age=int((now.year+(now.month/12.0))-(1984+birthday))
						%>
						Sina is a ${age} year old computer scientist, PhD survivor. He is a part of the 
						<a href="http://www.iam.ecs.soton.ac.uk">IAM research group</a> of 
						the <a href="http://ecs.soton.ac.uk">School of Electronics and Computer Science</a> 
						at the  <a href="http://www.soton.ac.uk">University of Southampton</a>. 
						He did his PhD in the <a href="http://www.iam.ecs.soton.ac.uk">ISIS research group</a> with
						<a href="http://www.ecs.soton.ac.uk/~msn">Prof. Mark S. Nixon</a> on <a href="http://eprints.ecs.soton.ac.uk/20895/">Semantic Biometric</a>.
						Sina's research interests include computer vision, machine learning, biometrics, semantic annotations and human annotation (both of and by). 
						He likes programming (lots of kinds), 
						juggling (lots of things), 
						music (lots of types), 
						friends, 
						philosophy 
						and the sun.
					</p>
					<p>You can find <a href="${h.url_for(controller='cv')}">Sina's CV here</a></p>
				</div>
				<div class="structure">
					<h3><strong>while</strong> <em>I work on...</em></h3>
					<div id="recentPubs">
						
					</div>
				</div>
				<div class="structure">
					<h3><strong>also</strong> <em>starring in...</em></h3>
					<ul>
						<li><strong><a href="http://twitter.com/sinjax">Twitter</a></strong></li>
						<li><strong><a href="http://facebook.com/sinjax">Facebook</a></strong></li>
					</ul>
				</div>
				<%include file="/sidebar/tagcloud.mako"/>
			</div>
			
		</div>
		<div id="bottombar">
			<p>Stolen, torn apart, slapped together and otherwise created by Sina Samangooei. Licensed under <a class="whitelink" href="http://sam.zoy.org/wtfpl/">WTFPL</a>
			% if "user" in session and session["user"]:
			<a href="${h.url_for('/logout')}"> logout </a>
			% else:
			<a href="${h.url_for('/login')}"> login </a>
			% endif
			</p>
		</div>
	</body>
</html>
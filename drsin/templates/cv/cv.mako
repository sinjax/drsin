<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
	"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">	
<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
	<title>Curriculum Vitae for Sina Samangooei</title>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js" type="text/javascript" charset="utf-8"></script>
	<script type="text/javascript" charset="utf-8">
		$(function () {
			$("#publications").load("${h.url_for(controller="style",action="recentPubs")} .citation")
			
		})
	</script>
<style type="text/css" media="screen">

body{
	margin: 0 auto;
}
.page{
	width:210mm;
	border:2px solid black;
	margin: 0 auto;
	margin-top:20mm;
}
h1{
	margin-top:2em;
}
#validXHTML{
	display:block;
}
</style>
<style type="text/css" media="print">
	#validXHTML{
		display:none;
	}
</style>
<style type="text/css" media="all">
*{
	margin:0;
	padding:0;
}

h1,h2,ul,p{
	font-family: "Helvetica", serif;
}
.layout{
	margin:1cm;
}
p, li, li *
{
	line-height:150%;
}
h1{
	margin-bottom:2em;
	text-align:center;
}

h2{
	font-size:16pt;
	border-bottom:2px solid black;
	margin-bottom:0.5em;
}
h3{
	font-size: 10pt;
	text-decoration: underline;
	padding-bottom:0.5em;
	position:relative;
}
h4{
	padding-top:1em;
}

.page>ul{
	padding-left:1em;
	margin-bottom:1em;
}
.layout>ul>li,p{
	font-size: 10pt;
	padding-bottom:0.5em;
	list-style: none;
}
.layout>ul>li>ul{
	font-size: 10pt;
	margin-left:1em;
}
h2.p_details{
	display:none;
}
ul.p_details{
	border:none;
	padding:0;
	margin:0;
	position:relative;
	top:-2em;
}
ul.p_details>li{
	padding:0;
	margin:0 auto;
	padding-left:2.5em;
	width:100mm;
	
}
ul.p_details>li>*{
	display:inline;
	left:0;
}
.nolist{
	list-style: none;
	position:relative;
	left:-1em;
}

.location_dates{
	position:absolute;
	left:0;
	width:100%;
	text-align: right;
	left:0;
}

.dates{
	float:right;
	clear:both;
	vertical-align: top;
}

.referee_name{
	font-size:120%;
}
.referee_address{
	font-size:90%;
}
</style>
</head>
<body  id="body">
	<div class="page">
		<div class="layout">
		<h1>
			Curriculum Vitae for <br/> Dr. Sina Samangooei
		</h1>
		<h2 class="p_details">Personal Details</h2>
		<ul class="p_details">
			<li>
				<h3>Nationality</h3>
				<p>British</p>
			</li>
			<li>
				<h3>Date of Birth</h3>
				<p>1984</p>
			</li>
			<li>
				<h3>Address</h3>
				<p>28 Oakmount Avenue, Southampton, UK, S017 1DR</p>
			</li>
			<li>
				<h3>E-mail</h3>
				<p>ss@ecs.soton.ac.uk</p>
			</li>
		</ul>
			
			<h2>Education</h2>
			<ul>
				<li>
					<h3>
						PhD in Computer Science <br/>
						<span class="location">University of Southampton</span>
						<span class="location_dates">
							<span class="dates">2006 - 2010</span>
						</span>
					</h3>
					<ul>
						<li class="nolist"><strong>Title:</strong> <a href="http://eprints.soton.ac.uk/153901/">Semantic Biometrics</a></li>
					    <li class="nolist"><strong>Supervisor:</strong> Prof. M. S. Nixon</li>
					    <li>Explored the ability of human understandable semantic descriptions towards improved identification and retrieval of individuals in biometrics enabled surveillance applications</li>
					    <li>Designed a system for efficient gathering and storage of semantic human descriptions against arbitrary biometric sources, integrating the system with Southampton Biometric Tunnel project while aiding in its development</li>
					    <li>Designed algorithms for effective fusion of semantic terms with automatic visual components, displaying improved recognition of individuals when human semantic descriptions are considered</li>
					    <li>Developed the first algorithms for the automatic semantic annotation of biometric data sources, demonstrating the ability of such approaches when applied to both existing and novel gait biometric datasets.</li>
					</ul>
				</li>
				<li>
					<h3>
					<span class="doing">MEng Computer Science, First Class</span><br/>
					<span class="location">University of Southampton</span>
					<span class="location_dates">
					<span class="dates">2002 - 2006</span>
					</span>
					</h3>
					
					<h4>Dissertation</h4>
					<p><em>Content Based Image Comparison and Retrieval using Sketch Analysis.</em> A full system, from feature extraction to integration with existing web image sources, for retrieving images using a quick sketch as the query.</p>
					
					<h4>Industrial Group Project</h4>
					<p><em>Obstruction management at Southampton Airport</em>. A visualisation tool for management of runway dimension re-declaration on event of obstructions. A simplified version of the completed project formed the skeleton for a second year group project assigned to BSc Computer Scientists that year.</p>
					
					<h4>Individual Research Project</h4>
					<p><em>A review of automatic annotation and semi-automatic annotation techniques in multimedia</em>. An exploration of the state of the art for annotation of music, images and videos. This included fully automatic techniques as well as approaches where automatic techniques assisted manual annotation</p>
					
					<h4>Selected modules/achievements:</h4>
					<ul>
						<li><em>Operating Systems</em> producing a 32-Bit Real-time Operating System using C</li>
						<li><em>Communications and Networks</em> producing a HTTP web-server using Java</li>
						<li><em>Interactive Entertainment Systems</em> producing a fully playable computer game using C++/OpenGL</li>
					</ul>
				</li>
				<li>
					<h3>
					<span class="doing">A levels</span><br/>
					<span class="location">Greenshaw High School</span>
					<span class="location_dates">
					<span class="dates">2000 - 2002</span></span>
					</h3>
					
					<p>A level Maths (A), Physics (A), ICT (A). AS level Economics (B)</p>
				</li>
			</ul>
			<h2>Research Interests</h2>
			<p>
				The development and application of novel approaches in Machine Learning and Computer Vision to address the exploration and effective utilisation of Large Scale Multimedia Corpa by humans, including: Multimedia retrieval through semantic and content based queries; Automatic annotation of multimedia artifacts towards machine understanding of scenes and objects; Human and Object recognition for applications in pervasive computing and surveillance.
			</p>
			<h2>Professional Experience</h2>
			<ul>
				<li>
					<h3>
					<span class="doing">Research Fellow</span><br/>
					<span class="location">University of Southampton</span>
					<span class="location_dates">
					<span class="dates">2010 - present</span></span>
					</h3>
					<ul>
						<li>Investigating scalable solutions for large-scale image retrieval tasks</li>
						<li>Exploring robust techniques for automatic image understanding</li>
						<li>Developing a suite of web services providing access to such algorithms for third party application development</li>
					</ul>
				</li>
				<li>
					<h3>
					<span class="doing">Research Assistant</span><br/>
					<span class="location">University of Southampton</span>
					<span class="location_dates">
					<span class="dates">2009 - 2010</span></span>
					</h3>
					<ul>
						<li>Web developer on the Lifeguide research project</li>
						<li>Assisted in the construction of community features of the lifeguideonline.org website</li>
						<li>Developed several key components of jQTI, a Java implementation of the QTI question/answer specification</li>
					</ul>
				</li>
				<li>
					<h3>
					<span class="doing">Technical Research Staff</span><br/>
					<span class="location">University of Southampton</span>
					<span class="location_dates">
					<span class="dates">Summer 2005</span></span>
					</h3>
					<ul>
						<li>Performed initial research on the EU funded eChase project </li>
						<li>Created the ﬁrst prototype of the Mediaengine portion of the eChase system </li>
						<li>Wrote Java interface with backing C++ FVS content based image comparison algorithms</li>
						<li>Wrote web service interface allowing FVS algorithm traversal of large image collections and comparisons of collections with provided inputs</li>
					</ul>
				</li>
				<li>
					<h3>
					<span class="doing">Technical Staff</span><br/>
					<span class="location">IT-Innovation</span>
					<span class="location_dates">
					<span class="dates">Summer 2004</span></span>
					</h3>
					<ul>
						<li>Joined ﬁnal portions of the EU funded Sculpteur project </li>
						<li>Improved the JSP Based interface </li>
						<li>Created multiple front ends in CSS for the system to match designs used by project partners (e.g. V&amp;A Museum)</li>
					</ul>
				</li>
			</ul>
			<h2>Skills</h2>
			<ul>
				<li>
					<h3>
					<span class="doing">Technical Skills</span>
					</h3>
					<ul>
						
						<li><strong>Highly skilled programmer</strong>. Experience in <strong>Java</strong> (and other JVM lanauges including <strong>Groovy</strong>), <strong>Python</strong> and <strong>C++</strong> along with experience in <strong>Matlab</strong>, <strong>Ruby</strong>, <strong>Prolog</strong> and <strong>Scheme</strong> </li>
						<li>Experienced database administrator, highly skilled in SQL with some experience with ORM database models (e.g. SQLAlchemy)</li>
						<li><strong>Experienced web programmer</strong>. Confident in both server side programming (<strong>Grails</strong>, <strong>PHP</strong>, <strong>JSP</strong> and <strong>Pylons</strong>) as well as client side scripting (<strong>javascript</strong>+<strong>jQuery</strong>, <strong>HTML</strong> and <strong>CSS</strong>)</li>
						<li>Confident unix programmer and administrator with experience using most shell tools</li>
						<li>Extensive experience with MS Windows (all versions), Mac OS (Tiger and Leopard) and many Linux environments</li>
					</ul>
				</li>
				<li>
					<h3>
					<span class="doing">Other Positions of Responsibility</span>
					</h3>
					<ul>
						<li>President of the Southampton University Circus Society, 2005</li>
						<li>Co-organiser of the ISIS Postgraduate Conference 2008</li>
					</ul>
				</li>
			</ul>
			<h2>Participation in Recent Research Projects</h2>
			<ul>
				<li>
					<h3>
					<span class="doing">LivingKnowledge (€4,900,000 – EU/IST [FP7])</span><br/>
					<span class="location">Research Fellow</span>
					<span class="location_dates">
					<span class="dates">2010 - 2012</span></span>
					</h3>
					<p>Currently employed 1/2 FTE on this project</p>
				</li>
				<li>
					<h3>
					<span class="doing">LiveMemories (€3,900,000 – The autonomous province of Trentino, Italy)</span><br/>
					<span class="location">Research Fellow</span>
					<span class="location_dates">
					<span class="dates">2010 - 2011</span></span>
					</h3>
					<p>Currently employed 1/2 FTE on this project</p>
				</li>
			</ul>
			<h2>Teaching Experience</h2>
			<p>Given guest lectures to 3rd year undergraduate students on the “Multimedia systems” course in 2009 and 2010. </p>
			<p>Some involvement in supervision of 3rd year undergraduate individual research projects (IRP).</p>
			<p>Teaching and Marking (since 2007) in 1st year computer science courses including Data Structures and Algorithms.</p>
			<p>Attended Teaching for Research Staff introductory course (2011)</p>
			
			<h2>Publications In Progress</h2>
			<p class="citation">Hare, J., Samangooei, S., Dupplaw, D., Lewis, P. ImageTerrier: A platform for scalable high-performance image retrieval. Submitted to: <em>ACM MM'11: ACM Multimedia</em>, November 28th 2011, Scottsdale, Arizona, USA. (submitted)</p>
			<p class="citation">Hare, J., Samangooei, S., Lewis, P. Introducing OpenImaJ: An open source image processing and retrieval library written entirely in java. Submitted to: <em>ACM MM'11: ACM Multimedia. Open Source Competition</em>, November 28th 2011, Scottsdale, Arizona, USA. (in progress)</p>
			<p class="citation">Samangooei, S., Hare, J., Lewis, P. Massively Parallel Image Retrieval using Hadoop. (in progress)</p>
			<h2>Publications</h2>
			<p id="publications">
				
			</p>
			<h2>Referees</h2>
			<ul>
				<li>
					<span class="referee_name">Professor Mark S. Nixon</span>
					<p class="referee_address">Information: Signals, Images, Systems Research Group, School of Electronics and Computer Science, University of Southampton, Southampton, Hampshire, SO17 1BJ Phone: +44 (0)23 8059 3542 • E-Mail: msn@ecs.soton.ac.uk</p>
				</li>
				<li>
					<span class="referee_name">Professor Paul Lewis</span>
					<p class="referee_address">Intelligence, Agents, Multimedia Group, School of Electronics and Computer Science, University of Southampton, Southampton, Hampshire, SO17 1BJ Phone: +44 (0)23 8059 3715 • E-Mail: phl@ecs.soton.ac.uk</p>
				</li>
				<li>
					<span class="referee_name">Dr Gary Willis</span>
					<p class="referee_address">Learning Societies Lab, School of Electronics and Computer Science, University of Southampton, Southampton, Hampshire, SO17 1BJ Phone: +44 (0)23 8059 2831 • E-Mail: gbw@ecs.soton.ac.uk </p>
				</li>
			</ul>
			</div>
	</div>
</body>
</html>

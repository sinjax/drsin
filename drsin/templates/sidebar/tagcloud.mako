<style type="text/css" media="screen">
	.tagcloud li{
		float:left;
		padding-right:1em;
	}
	.tagcloud li *{
		text-decoration: none;
	}
</style>
<script type="text/javascript" charset="utf-8">
	$(document).ready(function () {
		max = 0;
		maxFont = 18
		minFont = 8
		$(".tagcloud li").each(function (name,thing) {
			worth = parseInt($(thing).attr("worth"))
			if(worth > max) max = worth
		})
		$(".tagcloud li").each(function (name,thing) {
			worth = $(thing).attr("worth")
			weight = worth / max
			fontSize = minFont + ((maxFont - minFont) * weight)
			$(thing).css("font-size",fontSize+"pt")
		})
	})
</script>
<div class="structure">
	<h3><strong>things</strong> <em>talked about...</em></h3>
	<ul class="tagcloud">
	% for cat in c.cats:
	<li worth="${len(cat.posts)}"><a href="${h.url_for(controller='category',action='show',category=cat.category)}">${cat.category}</a></li>
	% endfor
	</ul>
</div>
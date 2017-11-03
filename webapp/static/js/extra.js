function append_post(parent_element, post)
{
    var html =\
'<article id="{0}" class="post">\
    <div class="post-head">\
        <h1 class="post-title"><a href="{1}">{2}</a></h1>\
        <div class="post-meta">\
            <time class="post-date">{3}</time>\
            |\
            标签 <a href="javascript:void(0);">{4}</a>\
        </div>\
    </div>\
    <div class="post-content">{5}</div>\
    <div class="post-permalink">\
        <a href="{6}" class="btn btn-default">阅读全文</a>\
    </div>\
    <footer class="post-footer clearfix">\
        <div class="pull-left tag-list">\
            <i class="fa fa-folder-open-o"></i>\
        </div>\
        <div class="pull-right share"></div>\
    </footer>\
</article>'.format(post.id, post.link, post.title, post.timestamp, post.tags, post.content, post.link)

    $("#" + parent_element).append(html);
}

function append_posts(parent_element, post_type, post_number)
{
    $("#" + parent_element).empty()
    $.ajax({
        type: "get",
        url: "/pubapi/get_posts",
        data: "type=" + post_type + "&num=" + post_number,
        async: true,
        success: function(data){
            var jsonList = JSON.parse(data)
            var len = jsonList.length;
            for(var i = 0 ; i < len ; i++){
                var post = jsonList[i];
                append_post(parent_element, post)
            }
        },
    });
}

function render_about(parent_element)
{
    $("#" + parent_element).empty()
    $.ajax({
        type: "get",
        url: "/pubapi/get_posts",
        data: "type=about&num=1",
        async: true,
        success: function(data){
            var jsonList = JSON.parse(data)
            var len = jsonList.length;
            for(var i = 0 ; i < len ; i++){
                var post = jsonList[i];
                render_post(parent_element, post)
            }
        },
    });
}

function render_post(parent_element, post_post)
{
    var html =\
'<article id="{0}" class="post">\
    <div class="post-head">\
        <h1 class="post-title"><a href="{1}">{2}</a></h1>\
        <div class="post-meta">\
            <time class="post-date">{3}</time>\
            |\
            标签 <a href="javascript:void(0);">{4}</a>\
        </div>\
    </div>\
    <div class="post-content">{5}</div>\
    <div class="post-permalink">\
        <a href="{6}" class="btn btn-default">阅读全文</a>\
    </div>\
    <footer class="post-footer clearfix">\
        <div class="pull-left tag-list">\
            <i class="fa fa-folder-open-o"></i>\
        </div>\
        <div class="pull-right share"></div>\
    </footer>\
</article>'.format(post.id, post.link, post.title, post.timestamp, post.tags, post.content, post.link)

    $("#" + element_id).empty();
    $("#" + element_id).append(html);
}
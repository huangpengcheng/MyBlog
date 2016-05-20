from django.db import models



class Article_Tag(models.Model):
    name = models.CharField('TagName',max_length=12)
    def  __str__(self):
        return self.name
class Article_genre(models.Model):
    name = models.CharField('GenreName',max_length=12)
    def  __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=254)
    content = models.TextField('内容')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    tag = models.ForeignKey(Article_Tag)
    genre = models.ForeignKey(Article_genre)

    def __str__(self):
        return self.title


# Article_Tag.objects.all()[0].article_set.all()
# a.tag = hello
# (tag=hello)

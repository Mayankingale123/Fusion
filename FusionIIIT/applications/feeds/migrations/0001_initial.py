# Generated by Django 3.1.5 on 2023-01-18 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('Mechanical', 'Mechanical'), ('Technical-Clubs', 'Technical Clubs'), ('Cultural-Clubs', 'Cultural Clubs'), ('Sports-Clubs', 'Sports Clubs'), ('Business-and-Career', 'Business and Career'), ('Entertainment', 'Entertainment'), ('IIITDMJ-Campus', 'IIITDMJ Campus'), ('Jabalpur-city', 'Jabalpur city'), ('IIITDMJ-Rules-and-Regulations', 'IIITDMJ rules and regulations'), ('Academics', 'Academics'), ('IIITDMJ', 'IIITDMJ'), ('Life-Relationship-and-Self', 'Life Relationship and Self'), ('Technology-and-Education', 'Technology and Education'), ('Programmes', 'Programmes'), ('Others', 'Others'), ('Design', 'Design')], default='CSE', max_length=100)),
                ('subtag', models.CharField(choices=[('Web-Development', 'Web Development'), ('Competitive-Programming', 'Competitive Programming'), ('Programming-Languages', 'Programming-Languages'), ('Data-Science', 'Data-Science'), ('Ethical-Hacking-and-Cyber-Security', 'Ethical hacking and cyber security'), ('Cryptography-and-Network-Security', 'cryptography and network security'), ('Software-Engineering', 'Software-Engineering'), ('Algorithm', 'Algorithm'), ('Mobile-Development', 'Mobile-Development'), ('Game-Development', 'Game-Development'), ('Artificial-Intelligence', 'Artificial Intelligence'), ('Electronics-Circuit-Design', 'Electronics Circuit Design'), ('Wireless-Communication', 'Wireless Communication'), ('Embedded-System', 'Embedded Systems'), ('VLSI', 'VLSI'), ('Control-System', 'Control Systems'), ('Robotics-and-others', 'Robotics and Others'), ('Microcontrollers', 'Microcontrollers'), ('IOT', 'IOT'), ('Robotics', 'Robotics'), ('Thermodynamics', 'Thermodynamics'), ('Nanatechnology', 'Nanatechnology'), ('Manufacturing', 'Manufacturing'), ('Programming-and-Webix-Club', 'Programming and Webix Club'), ('Electronics-Club', 'Electronics Club'), ('Business-and-Management-Club', 'Business and Management Club'), ('Robotics-Club', 'Robotics Club'), ('CAD-Club', 'CAD Club'), ('Astronomy-and-Physics-Society', 'ASTRONOMY AND PHYSICS SOCIETY'), ('Aakriti-The-Film-Making-and-Photography-Club', 'AAKRITI-THE FILM MAKING AND PHOTOGRAPHY CLUB'), ('AUTOMOTIVE-AND-FABRICATION-CLUB', 'AUTOMOTIVE AND FABRICATION CLUB'), ('RACING-CLUB', 'RACING CLUB'), ('SAAZ-MUSIC-CLUB', 'SAAZ-MUSIC CLUB'), ('SAMVAAD-THE-LITERATURE-AND-QUIZZING-SOCIETY', 'SAMVAAD-THE LITERATURE AND QUIZZING SOCIETY'), ('ABHIVYAKTI-ARTS-CLUB', 'ABHIVYAKTI-ARTS CLUB'), ('JAZBAAT-THE-DRAMATICS-SOCIETY', 'JAZBAAT-THE DRAMATICS SOCIETY'), ('AAVARTAN-DANCE-CLUB', 'AAVARTAN-DANCE CLUB'), ('BADMINTON-CLUB', 'BADMINTON CLUB'), ('LAWN-TENNIS-&-BASKETBALL-CLUB', 'LAWN TENNIS&BASKETBALL CLUB'), ('TABLE-TENNIS', 'TABLE TENNIS'), ('CHESS-&-CARROM-CLUB', 'CHESS & CARROM CLUB'), ('CRICKET-CLUB', 'CRICKET CLUB'), ('FOOTBALL-CLUB', 'FOOTBALL CLUB'), ('VOLLEYBALL-CLUB', 'VOLLEYBALL CLUB'), ('ATHLETICS-CLUB', 'ATHLETICS CLUB'), ('Business-Models-and-Strategies', 'Business Models and strategies'), ('Startups-and-Stratup-Strategies', 'Startups and Stratup Strategies'), ('Entrepreneurship', 'Entrepreneurship'), ('Finance', 'Finance'), ('Marketing', 'Marketing'), ('Stock-Market', 'Stock market'), ('Career-Advice', 'Career Advice'), ('Job-Interviews', 'Job Interviews'), ('Journalism', 'Journalism'), ('Entertainment', 'Entertainment'), ('Hollywood-and-Movies', 'Hollywood and Movies'), ('Music', 'Music'), ('Fashion-and-Style', 'Fashion and Style'), ('IIITDMJ-Campus', 'IIITDMJ-Campus'), ('Jabalpur-City', 'Jabalpur City'), ('IIITDMJ-rules-and-Regulations', 'IIITDMJ rules and regulations'), ('Academic-Office-Stuffs', 'Academic office stuffs'), ('Academic-Courses', 'Academic courses'), ('Central-Mess', 'Central Mess'), ('Alumni', 'Alumni'), ('Hostels', 'Hostels'), ('PHC', 'PHC'), ('Activities', 'Activities'), ('Counselling', 'Counselling'), ('Achievments', 'Achievments'), ('Library', 'Library'), ('Faculty', 'Faculty'), ('Staff', 'Staff'), ('College-Fest', 'College Fest'), ('Workshops', 'Workshops'), ('Campus-Recruitments', 'Campus Recruitments'), ('Jagrati', 'Jagrati'), ('Self-Improvement', 'Self Improvement'), ('Friendship', 'Friendship'), ('Experiences', 'Experiences'), ('Dating-and-Relationships', 'Dating and Relationships'), ('Interpersonal-Interactions', 'Interpersonal Interactions'), ('Life-and-Social-Advice', 'Life and Social Advice'), ('Philosophy', 'Philosophy'), ('Technology-Trends', 'Technology Trends'), ('TED', 'TED'), ('Higher-Education', 'Higher Education'), ('Science-and-Universe', 'Science and Universe'), ('Social-Media', 'Social-Media'), ('Toron', 'Toron'), ('Jobs-and-Internships', 'Jobs and Internships'), ('Btech', 'Btech'), ('Mtech', 'Mtech'), ('Bdes', 'Bdes'), ('Mdes', 'Mdes'), ('Phd', 'Phd'), ('Mechatronics', 'Mechatronics'), ('others', 'others')], default='Web-Development', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AskaQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_delete', models.BooleanField(default=False)),
                ('can_update', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='feeds/files')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_liked', models.BooleanField(default=False)),
                ('is_requested', models.BooleanField(default=False)),
                ('request', models.IntegerField(default=0)),
                ('anonymous_ask', models.BooleanField(default=False)),
                ('dislikes', models.ManyToManyField(blank=True, default=1, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, default=1, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('requests', models.ManyToManyField(blank=True, default=1, related_name='requests', to=settings.AUTH_USER_MODEL)),
                ('select_tag', models.ManyToManyField(to='feeds.AllTags')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=5000)),
                ('commented_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_liked', models.BooleanField(default=False)),
                ('likes_comment', models.ManyToManyField(blank=True, default=1, related_name='likes_comment', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.askaquestion')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_msg', models.CharField(default='', max_length=1000)),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.askaquestion')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=1000)),
                ('content', models.CharField(default='', max_length=5000)),
                ('replied_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.comments')),
                ('replies', models.ManyToManyField(blank=True, default=1, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAccessControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canVote', models.BooleanField()),
                ('canAnswer', models.BooleanField()),
                ('canComment', models.BooleanField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('posted_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.roles')),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question_list', to='feeds.askaquestion')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=250)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='feeds/profile_pictures')),
                ('profile_view', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnsweraQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000)),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_liked', models.BooleanField(default=False)),
                ('answers', models.ManyToManyField(blank=True, default=1, related_name='answers', to=settings.AUTH_USER_MODEL)),
                ('dislikes', models.ManyToManyField(blank=True, default=1, related_name='answer_dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, default=1, related_name='answer_likes', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.askaquestion')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_tag', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('Mechanical', 'Mechanical'), ('Technical-Clubs', 'Technical Clubs'), ('Cultural-Clubs', 'Cultural Clubs'), ('Sports-Clubs', 'Sports Clubs'), ('Business-and-Career', 'Business and Career'), ('Entertainment', 'Entertainment'), ('IIITDMJ-Campus', 'IIITDMJ Campus'), ('Jabalpur-city', 'Jabalpur city'), ('IIITDMJ-Rules-and-Regulations', 'IIITDMJ rules and regulations'), ('Academics', 'Academics'), ('IIITDMJ', 'IIITDMJ'), ('Life-Relationship-and-Self', 'Life Relationship and Self'), ('Technology-and-Education', 'Technology and Education'), ('Programmes', 'Programmes'), ('Others', 'Others'), ('Design', 'Design')], default=1, max_length=100)),
                ('my_subtag', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.alltags')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'my_subtag')},
            },
        ),
        migrations.CreateModel(
            name='hidden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.askaquestion')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'question')},
            },
        ),
    ]

from app.models.user import User
from app.models.message import Message
from app.models.city import City
from app import db
from flask import request,render_template,redirect,url_for
from app.views import frontend
from . import frontend




@frontend.route('/create', methods=["POST", "GET"])
def create():
    # 建立資料表
    db.create_all()

    # 在Message()這張表單新增資料
    create_Taipei_Messags = City(name='Taipei')
    db.session.add(create_Taipei_Messags)  # 建立資料暫存

    create_New_Taipei_Messags = City(name='New Taipei')
    db.session.add(create_New_Taipei_Messags)  # 建立資料暫存

    create_Taoyuan_Messags = City(name='Taoyuan')
    db.session.add(create_Taoyuan_Messags)  # 建立資料暫存

    create_Taichung_Messags = City(name='Taichung')
    db.session.add(create_Taichung_Messags)  # 建立資料暫存

    create_Tainan_Messags = City(name='Tainan')
    db.session.add(create_Tainan_Messags)  # 建立資料暫存

    create_Kaohsiung_Messags = City(name='Kaohsiung')
    db.session.add(create_Kaohsiung_Messags)  # 建立資料暫存
    db.session.commit()  # 傳送至資料庫

    create_user = User(city_id='1', name='deemo')  # 建立一個deemo
    db.session.add(create_user)  # 建立資料暫存
    db.session.commit()  # 傳送至資料庫


    return '建立資料庫成功:內建Taipei、New Taipei、Taoyuan、Taichung、Tainan、Kaohsiung'


@frontend.route('/drop', methods=["POST", "GET"])
def drop():
    db.drop_all()
    return render_template('drop.html')



@frontend.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        content = request.form['content']
        title = request.form['title']
        add_name = request.form['add_name']


        select_user = User.query.filter_by(name=add_name)  # 先取得在user當中naem='Eric'的User_id

        # 在Message()這張表單新增資料
        create_Eric_Messags = Message(user_id=select_user[0].id, title=title, content=content)
        db.session.add(create_Eric_Messags)  # 建立資料暫存
        db.session.commit()  # 傳送至資料庫

        # 因為在frontend裡面，所以要加上前面的位置
        return redirect(url_for('frontend.Index'))

    return render_template('add.html')


@frontend.route('/update_db', methods=["POST", "GET"])  # 小心同名子不行
def update_db():
    if request.method == "POST":
        content = request.form['content']
        title = request.form['title']
        username = request.form['name']
        select_message_user = User.query.filter_by(name=username).first()
        select_messages = Message.query.filter_by(user_id=select_message_user.id)

        #依序更改select_message內的內容
        for select_message in select_messages:
            select_message.title = title
            select_message.content = content
        db.session.commit()

        # 這樣不用url_for的方法也是可以試試
        return redirect('update_db')

    return render_template('update.html', Message=Message.query.all())





@frontend.route('/delete/<message_id>', methods=['GET', 'POST'])
def delete(message_id):

    # 抓取message表單中id = message_id 的第一筆資料
    message_delete = Message.query.filter_by(id=int(message_id)).first()
    # 利用 delete 的方法即可刪除單筆資料
    db.session.delete(message_delete)
    # 將之前的操作變更至資料庫中
    db.session.commit()

    return redirect('/')


@frontend.route('/show', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        content = request.form['content']
        title = request.form['title']
        add_name = request.form['add_name']

        select_user = User.query.filter_by(name=add_name)  # 先取得在user當中naem='Eric'的User_id

        # 在Message()這張表單新增資料
        create_Eric_Messags = Message(user_id=select_user[0].id, title=title, content=content)
        db.session.add(create_Eric_Messags)  # 建立資料暫存
        db.session.commit()  # 傳送至資料庫


        return render_template('show.html', Message=Message.query.all())

    return render_template('show.html', Message=Message.query.all())


@frontend.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form["user_name"]
        user_city = request.form["city_select"]  # 獲得使用者的id

        #這段不要加
        if user_city =="6" and user_name =="deemo" :
            return redirect('show')
        #到這裡為止


        create_user = User(city_id=user_city,name=user_name)  # User()為要加入入的表單  # 必要條件為id(非必要),city_id(必要),name(必要)

        db.session.add(create_user)  # 建立資料暫存
        db.session.commit()  # 傳送至資料庫

        return render_template('Index.html', Message=Message.query.all())

    return render_template('register.html')



@frontend.route('/get_data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':

        res = User.query.all()
        res1 = City.query.all()

        return str(res)+"\n"+str(res1)

    return render_template('test.html')



@frontend.route('/dictionary', methods=["POST", "GET"])
def dictionary():
    movie = {'name': 'Saving Private Ryan',  # 電影名稱
             'year': 1998,  # 電影上映年份
             'director': 'Steven Spielberg',  # 導演
             'Writer': 'Robert Rodat',  # 編劇
             'Stars': ['Tom Hanks', 'Matt Damon', 'Tom Sizemore'],  # 明星
             'Oscar ': ['Best Director', 'Best Cinematography', 'Best Sound', 'Best Film Editing',
                        'Best Effects, Sound Effects Editing']
             # 獲得的奧斯卡獎項
             }

    return movie['Stars'][0]



@frontend.route('/', methods=["POST", "GET"])
def Index():
    if request.method == "POST":
        id_data = request.form['id']
        content = request.form['current_content']
        title = request.form['current_title']
        select_message = Message.query.filter_by(id=int(id_data)).first()
        select_message.title = title
        select_message.content = content
        db.session.commit()

        return render_template('Index.html', Message=Message.query.all())

    return render_template('Index.html', Message=Message.query.all())




@frontend.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        add_name = request.form["add_name"]
        title = request.form["title"]
        content = request.form["content"]
        select_user = User.query.filter_by(name=add_name)

        # 在Message()這張表單新增資料
        create_Messags = Message(user_id=select_user[0].id, title=title, content=content)
        db.session.add(create_Messags)  # 建立資料暫存
        db.session.commit()  # 傳送至資料庫

        return render_template('test.html', Message=Message.query.all())

    return render_template('test.html', Message=Message.query.all())
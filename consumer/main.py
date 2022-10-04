# Typer
# Click
# Google-fire

from github import Github
from config import settings
from sqlalchemy import Boolean, Column, create_engine
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column, Integer, String, Boolean

github = Github(settings.GITHUB_TOKEN)


repositories = github.search_repositories(
        query="topic:'flask-extension flask-extensions'",
        sort='stars'
)


engine = create_engine(settings.DATABASE_URI, echo=True)
session = sessionmaker(bind=engine)()
Base = declarative_base()


class Repo(Base):
    __tablename__ = 'repos'
    
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    full_name = Column(String)
    archived = Column(Boolean)
    html_url = Column(String)

    def __repr__(self) -> str:
        return f'User {self.full_name}'


# command
Base.metadata.create_all(engine)

for item in repositories:
    repo = Repo(id=item.id,
                name=item.name,
                full_name = item.full_name,
            html_url= item.html_url,
    )
    session.add(repo)

session.commit()

import connexion
import six


from swagger_server.controllers.DiaryDatabase import DiaryDatabase
from swagger_server.models.diary_entry import DiaryEntry  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util





def diaries_date_get(date):  # noqa: E501
    """Get diary entry by date

     # noqa: E501

    :param _date: 
    :type _date: str

    :rtype: DiaryEntry
    """

    date2 = util.deserialize_date(date)
    db = DiaryDatabase("diary.db")
    r=db.get_diary_by_date(date2)
    db.close()
    return r



def diaries_date_patch(date, body=None):  # noqa: E501
    """Update a diary entry

     # noqa: E501

    :param _date: 
    :type _date: str
    :param body: Diary entry to update
    :type body: dict | bytes

    :rtype: DiaryEntry
    """
    _date = util.deserialize_date(date)
    if connexion.request.is_json:
        body = DiaryEntry.from_dict(connexion.request.get_json())  # noqa: E501
    db = DiaryDatabase("diary.db")
    ret=db.update_diary(_date, body)
    db.close()
    return ret


def diaries_get():  # noqa: E501
    """Get all diary entries

     # noqa: E501


    :rtype: List[DiaryEntry]
    """
    db = DiaryDatabase("diary.db")

    ret=db.get_all_diaries()
    db.close()
    return ret


def diaries_post(body=None):  # noqa: E501
    """Create a new diary entry

     # noqa: E501

    :param body: Diary entry to create
    :type body: dict | bytes

    :rtype: DiaryEntry
    """
    if connexion.request.is_json:
        body = DiaryEntry.from_dict(connexion.request.get_json())  # noqa: E501
    db = DiaryDatabase("diary.db")
    ret=db.create_diary(body)
    db.close()
    return ret
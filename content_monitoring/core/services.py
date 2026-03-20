from .models import Keyword, ContentItem, Flag

def calculate_score(keyword, content):
    keyword = keyword.lower()
    title = content.title.lower()
    body = content.body.lower()

    if keyword == title:
        return 100
    elif keyword in title:
        return 70
    elif keyword in body:
        return 40
    return 0


def should_create_flag(keyword, content):
    existing_flag = Flag.objects.filter(
        keyword=keyword,
        content_item=content
    ).first()

    if not existing_flag:
        return True

    if existing_flag.status == 'irrelevant':
        if existing_flag.reviewed_at and content.last_updated <= existing_flag.reviewed_at:
            return False

    return True


def run_scan():
    mock_data = [
        {
            "title": "Learn Django Fast",
            "body": "Django is a powerful Python framework",
            "source": "Blog A",
            "last_updated": "2026-03-20T10:00:00Z"
        },
        {
            "title": "Cooking Tips",
            "body": "Best recipes for beginners",
            "source": "Blog B",
            "last_updated": "2026-03-20T10:00:00Z"
        }
    ]

    keywords = Keyword.objects.all()

    for item in mock_data:
        content, _ = ContentItem.objects.get_or_create(
            title=item['title'],
            defaults=item
        )

        for keyword in keywords:
            score = calculate_score(keyword.name, content)

            if score > 0 and should_create_flag(keyword, content):
                Flag.objects.update_or_create(
                    keyword=keyword,
                    content_item=content,
                    defaults={'score': score, 'status': 'pending'}
                )
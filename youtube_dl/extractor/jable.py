# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class JableIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?jable\.tv/([^/]+/)*(?P<id>[^/\?#]+)'
    _TESTS = [{
        'url': 'https://www.ora.tv/larrykingnow/2015/12/16/vine-youtube-stars-zach-king-king-bach-on-their-viral-videos-0_36jupg6090pq',
        'md5': 'fa33717591c631ec93b04b0e330df786',
        'info_dict': {
            'id': '50178',
            'ext': 'mp4',
            'title': 'Vine & YouTube Stars Zach King & King Bach On Their Viral Videos!',
            'description': 'md5:ebbc5b1424dd5dba7be7538148287ac1',
        }
    }, {
        'url': 'http://www.unsafespeech.com/video/2016/5/10/student-self-censorship-and-the-thought-police-on-university-campuses-0_6622bnkppw4d',
        'only_matching': True,
    }]

    def _real_extract(self, url):
        display_id = self._match_id(url)
        webpage = self._download_webpage(url, display_id)
        title = self._search_regex('<meta property="og:title" content="(.*?)" />',
            webpage, 'title', None)
        m3u8_url = self._search_regex(
            r'''var hlsUrl = '([^"]*?)';''', webpage, 'm3u8 url', None)
        formats = []
        if m3u8_url:
            formats.extend(self._extract_m3u8_formats(
                m3u8_url, display_id, 'mp4', entry_protocol='m3u8_native',
                m3u8_id='hls', fatal=False))
            from pprint import pprint;pprint(  formats)
        
        return {
            'id': 'video_id',
            'formats': formats,
            'title': title,
            # 'duration': duration,
            # 'thumbnails': thumbnails,
            'age_limit': 18,
        }

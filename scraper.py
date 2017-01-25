from dc_base_scrapers.xml_scraper import GmlScraper


stations_url = "http://mapsbcw.wellingborough.gov.uk/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer?service=WFS&version=1.1.0&request=GetFeature&typeNames=electoral_electoral_wfs%3APolling_Stations"
stations_fields = {
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}OBJECTID_12': 'OBJECTID_12',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}ADDRESS': 'ADDRESS',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}DISTRICTS': 'DISTRICTS',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}WEBSITE': 'WEBSITE',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}POLLING_PLACE': 'POLLING_PLACE',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}LOCATION_URL': 'LOCATION_URL',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}POINT_X': 'POINT_X',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}POINT_Y': 'POINT_Y',
}

districts_url = "http://mapsbcw.wellingborough.gov.uk/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer?service=WFS&version=1.1.0&request=GetFeature&typeNames=electoral_electoral_wfs%3APolling_Districts"
districts_fields = {
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}OBJECTID': 'OBJECTID',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}POLLING_DISTRICT_NAME': 'POLLING_DISTRICT_NAME',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}POLLING_DISTRICT_CODE': 'POLLING_DISTRICT_CODE',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}WEBSITE': 'WEBSITE',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}ADDRESS': 'ADDRESS',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}SHAPE.STArea___': 'SHAPE.STArea___',
    '{http://bcw-giscore.wellingborough.gov.uk:6080/arcgis/services/electoral/electoral_wfs/MapServer/WFSServer}SHAPE.STLength__': 'SHAPE.STLength__',
}

council_id = 'E07000156'


stations_scraper = GmlScraper(stations_url, council_id, 'stations', stations_fields, 'OBJECTID_12')
stations_scraper.scrape()
districts_scraper = GmlScraper(districts_url, council_id, 'districts', districts_fields, 'OBJECTID')
districts_scraper.scrape()

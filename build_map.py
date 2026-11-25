import json
from base64 import b64encode
from pathlib import Path

import geopandas as gpd


ROOT = Path(__file__).resolve().parent
DATA_SOURCE = ROOT / "data_src" / "data"
PROVINCE_SOURCE = Path(
    r"C:\Users\kubilay.selcuk\OneDrive - Bogazici Proje Muh AS\Yücel Erdem Dişli dosyaları - UlusalİltisakCalismasi\Database\İLLTİSAK_ÇALIŞMASI\02-Sınırlar\Türkiye_İlBazlı_Değerler.shp"
)
OUT = ROOT / "index.html"


def clean_value(value):
    if value is None:
        return ""
    text = str(value).strip()
    if text.lower() in {"", "nan", "none", "null"}:
        return ""
    fixes = {
        "\u00c4\u00b0": "İ",
        "\u00c4\u00b1": "ı",
        "\u00c5\u0178": "Ş",
        "\u00c5\u015f": "ş",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u017e": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u0178": "Ğ",
        "\u00c4\u011f": "ğ",
        "\u00c3\u0153": "Ü",
        "\u00c3\u00bc": "ü",
        "\u00c3\u2013": "Ö",
        "\u00c3\u00b6": "ö",
        "\u00c3\u2021": "Ç",
        "\u00c3\u00a7": "ç",
        "\u00c5": "Ş",
        "�LETMEDE": "ŞLETMEDE",
        "A�AMASINDA": "AŞAMASINDA",
        "KAMULA�TIRMA": "KAMULAŞTIRMA",
        "BAKANLI�I": "BAKANLIĞI",
        "�ef": "Şef",
        "�stasyon": "İstasyon",
        "�ırnak": "Şırnak",
        "yatırmı": "yatırımı",
        "As�m": "Asım",
    }
    for old, new in fixes.items():
        text = text.replace(old, new)
    return text


def clean_value(value):
    if value is None:
        return ""
    text = str(value).strip()
    if text.lower() in {"", "nan", "none", "null"}:
        return ""
    fixes = {
        "\u00c4\u00b0": "İ",
        "\u00c4\u00b1": "ı",
        "\u00c4\u011f": "ğ",
        "\u00c5\u015f": "ş",
        "\u00c3\u00bc": "ü",
        "\u00c3\u00b6": "ö",
        "\u00c3\u00a7": "ç",
        "\u00c4\u00b0\u00c5": "İŞ",
        "\u00c5ef": "Şef",
        "\u00c5stasyon": "İstasyon",
        "A\u00c5AMASINDA": "AŞAMASINDA",
        "KAMULA\u00c5TIRMA": "KAMULAŞTIRMA",
        "�LETMEDE": "ŞLETMEDE",
        "A�AMASINDA": "AŞAMASINDA",
        "KAMULA�TIRMA": "KAMULAŞTIRMA",
        "�ef": "Şef",
        "�stasyon": "İstasyon",
        "As�m": "Asım",
    }
    for old, new in fixes.items():
        text = text.replace(old, new)
    return text


def clean_value(value):
    if value is None:
        return ""
    text = str(value).strip()
    if text.lower() in {"", "nan", "none", "null"}:
        return ""
    fixes = {
        "Ã‡": "Ç",
        "Ã§": "ç",
        "Ã–": "Ö",
        "Ã¶": "ö",
        "Ãœ": "Ü",
        "Ã¼": "ü",
        "Ä°": "İ",
        "Ä±": "ı",
        "ÄŸ": "ğ",
        "Äž": "Ğ",
        "Åž": "Ş",
        "ÅŸ": "ş",
        "â€“": "-",
        "â€”": "-",
        "â€˜": "'",
        "â€™": "'",
        "â€œ": '"',
        "â€": '"',
        "â€": '"',
        "Â ": " ",
        "Â": "",
        "\u00c4\u00b0": "İ",
        "\u00c4\u00b1": "ı",
        "\u00c4\u0178": "ğ",
        "\u00c4\u017e": "Ğ",
        "\u00c3\u00b6": "ö",
        "\u00c3\u00bc": "ü",
        "\u00c3\u00a7": "ç",
        "\u00c3\u2016": "Ö",
        "\u00c3\u0153": "Ü",
        "\u00c3\u2021": "Ç",
        "\u00c5\u0178": "ş",
        "\u00c5\u015f": "ş",
        "\u00c5\u017e": "Ş",
        "ÄI": "ĞI",
        "Äİ": "Ğİ",
        "Äi": "ği",
        "\u00c5": "Ş",
        "�LETMEDE": "ŞLETMEDE",
        "A�AMASINDA": "AŞAMASINDA",
        "KAMULA�TIRMA": "KAMULAŞTIRMA",
        "�N�AAT": "İNŞAAT",
        "�n�aat": "İnşaat",
        "SANAY�": "SANAYİ",
        "BAKANLI�I": "BAKANLIĞI",
        "�ef": "Şef",
        "�stasyon": "İstasyon",
        "As�m": "Asım",
    }
    for old, new in fixes.items():
        text = text.replace(old, new)
    return text


def normalize_key(text):
    return (
        clean_value(text)
        .upper()
        .replace("İ", "I")
        .replace("İ", "I")
        .replace("Ş", "S")
        .replace("Ğ", "G")
        .replace("Ü", "U")
        .replace("Ö", "O")
        .replace("Ç", "C")
    )


def status_rail(value):
    key = normalize_key(value)
    if key == "MEVCUT":
        return "Mevcut"
    if key == "PROJE":
        return "Proje"
    if key == "INSAAT":
        return "İnşaat"
    if key == "PLAN":
        return "Plan"
    return clean_value(value) or "Diğer"


def status_osb(value):
    key = normalize_key(value)
    return "Mevcut" if "ISLETMEDE" in key else "Planlanan"


def osb_priority(value):
    text = clean_value(value)
    try:
        rank = int(float(text.replace(",", ".")))
    except ValueError:
        return {"rank": "", "className": "unknown", "label": "Öncelik bilgisi yok"}
    if rank <= 50:
        label = "1. Öncelik"
        class_name = "very-high"
    elif rank <= 150:
        label = "2. Öncelik"
        class_name = "high"
    elif rank <= 250:
        label = "3. Öncelik"
        class_name = "medium"
    elif rank <= 350:
        label = "4. Öncelik"
        class_name = "low"
    else:
        label = "5. Öncelik"
        class_name = "watch"
    return {"rank": rank, "className": class_name, "label": label}


def status_logistics(value):
    key = normalize_key(value)
    return "Mevcut" if "ISLETMEYE" in key else "Planlanan"


def status_connection(value):
    key = normalize_key(value)
    if key == "MEVCUT":
        return "Mevcut"
    if key == "PROJE":
        return "Proje"
    if key == "PLANLANAN":
        return "Planlanan"
    if key == "INSAAT":
        return "İnşaat"
    if key == "YATIRIM PROGRAMINDA":
        return "Yatırım Programında"
    return clean_value(value).title() or "Diğer"


def electric_label(value):
    key = clean_value(value).lower()
    return {
        "contact_line": "Katener",
        "no": "Elektriksiz",
        "yes": "Elektrikli",
        "rail": "Ray hattı üzerinden besleme",
    }.get(key, clean_value(value))


def round_coords(obj, places=5):
    if isinstance(obj, (list, tuple)):
        if obj and isinstance(obj[0], (int, float)):
            return [round(float(v), places) for v in obj[:2]]
        return [round_coords(v, places) for v in obj]
    return obj


def geometry_json(geom):
    return json.loads(gpd.GeoSeries([geom], crs="EPSG:4326").to_json())["features"][0]["geometry"]


def read_shp(pattern, encoding=None):
    matches = sorted(DATA_SOURCE.glob(pattern), key=lambda path: path.stat().st_mtime, reverse=True)
    if not matches:
        raise FileNotFoundError(f"{pattern} bulunamadı: {DATA_SOURCE}")
    kwargs = {"encoding": encoding} if encoding else {}
    return gpd.read_file(matches[0], **kwargs).to_crs("EPSG:4326")


def read_source(path, encoding=None):
    kwargs = {"encoding": encoding} if encoding else {}
    return gpd.read_file(path, **kwargs).to_crs("EPSG:4326")


def details_from_pairs(pairs, include_empty=False):
    details = []
    for label, value in pairs:
        cleaned = clean_value(value)
        if cleaned or include_empty:
            details.append({"label": label, "value": cleaned or "-"})
    return details


def normalized_columns(gdf):
    return {normalize_key(column): column for column in gdf.columns if column != "geometry"}


def row_by_key(row, column_map, *keys):
    for key in keys:
        column = column_map.get(normalize_key(key))
        if column:
            return row.get(column)
    return ""


def details_from_columns(row, columns, labels, skip_keys=(), include_empty=False):
    skip = {normalize_key(key) for key in skip_keys}
    pairs = []
    for column in columns:
        if column == "geometry" or normalize_key(column) in skip:
            continue
        label = labels.get(normalize_key(column), clean_value(column))
        pairs.append((label, row.get(column)))
    return details_from_pairs(pairs, include_empty=include_empty)


def feature_collection(records):
    return {"type": "FeatureCollection", "features": records}


def line_features(gdf, props_for_row, simplify=0.0009):
    records = []
    gdf = gdf.copy()
    gdf["geometry"] = gdf.geometry.simplify(simplify, preserve_topology=True)
    for _, row in gdf.iterrows():
        geom = row.geometry
        if geom is None or geom.is_empty:
            continue
        records.append({"type": "Feature", "geometry": geometry_json(geom), "properties": props_for_row(row)})
    return records


def polygon_features(gdf, props_for_row, simplify=0.001):
    records = []
    gdf = gdf.copy()
    gdf["geometry"] = gdf.geometry.simplify(simplify, preserve_topology=True)
    for _, row in gdf.iterrows():
        geom = row.geometry
        if geom is None or geom.is_empty:
            continue
        records.append({"type": "Feature", "geometry": geometry_json(geom), "properties": props_for_row(row)})
    return records


def point_features(gdf, props_for_row):
    records = []
    for _, row in gdf.iterrows():
        geom = row.geometry
        if geom is None or geom.is_empty:
            continue
        records.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": round_coords([geom.x, geom.y], 5)},
                "properties": props_for_row(row),
            }
        )
    return records


def railway_features():
    source = DATA_SOURCE / "demiryolu"
    if not source.is_dir():
        return legacy_railway_features()

    existing = read_source(source / "MEVCUT.shp").rename(columns={
        "HAT_ADI": "Ad",
        "TYPE": "Kurum",
        "uzunluk": "Km2",
    }).assign(TYPE="Mevcut")
    projects = read_source(source / "PLANPROJE_TEK_AKS.shp")

    def props(row):
        status = status_rail(row["TYPE"])
        name = clean_value(row["Ad"]) or "Demiryolu hattı"
        owner = clean_value(row["Kurum"])
        details = details_from_pairs([
            ("Hat adı", name),
            ("Kurum", owner),
            ("Uzunluk (km)", round(row["Km2"], 2)),
            ("Durum", clean_value(row.get("Durum")) or status),
        ])
        return {
            "layer": "rail",
            "status": status,
            "name": name,
            "owner": owner,
            "details": details,
            "searchText": " ".join(item["value"] for item in details),
        }

    return line_features(existing, props, simplify=0.0012) + line_features(projects, props, simplify=0.0012)


def legacy_railway_features():
    gdf = read_shp("Demiryolu*.shp", encoding="cp1254")
    columns = list(gdf.columns)
    labels = {
        "DURUM2": "Durum",
        "HAT_ADI": "Hat adı",
        "ISLETME": "İşletme",
        "HIZ": "Hız",
        "ELEKTRIK": "Elektrik",
        "YUKSEK_HIZ": "Yüksek hızlı",
    }

    def props(row):
        status = status_rail(row.get("DURUM2"))
        name = clean_value(row.get("HAT_ADI")) or "Demiryolu hattı"
        details = details_from_columns(row, columns, labels, skip_keys=("Durum", "Railway"))
        durum_items = [item for item in details if item["label"] == "Durum"]
        details = [item for item in details if item["label"] != "Durum"] + durum_items
        for item in details:
            if item["label"] == "Elektrik":
                item["value"] = electric_label(item["value"])
        return {"layer": "rail", "status": status, "name": name, "details": details, "searchText": " ".join(item["value"] for item in details)}

    return line_features(gdf, props, simplify=0.0012)


def connection_features():
    gdf = read_shp("İltisak*.shp", encoding="cp1254")
    columns = list(gdf.columns)
    column_map = normalized_columns(gdf)
    labels = {
        "IL_1": "İl",
        "KURUM_1": "Kurum",
        "AD_1": "Ad",
        "TUR_1": "Tür",
        "ACIKLAMA": "Açıklama",
        "DURUM": "Durum",
    }

    def props(row):
        status = status_connection(row_by_key(row, column_map, "Durum"))
        name = clean_value(row_by_key(row, column_map, "Ad_1", "Ad")) or "İltisak hattı"
        owner = clean_value(row_by_key(row, column_map, "Kurum_1", "Kurum")) or "PLANLANAN ÇALIŞMA YOK"
        details = details_from_columns(row, columns, labels, include_empty=True)
        return {"layer": "connection", "status": status, "name": name, "owner": owner, "details": details, "searchText": " ".join([owner, *(item["value"] for item in details)])}

    return line_features(gdf, props, simplify=0.0007)


def osb_features():
    gdf = read_shp("OSBUK_OSB_r02.shp", encoding="cp1254")
    columns = list(gdf.columns)
    column_map = normalized_columns(gdf)
    labels = {
        "SIRA_NO_1": "Sıra no",
        "OSB_ILI_1": "İl",
        "OSB_UNVA_": "OSB adı",
        "FIILI_DU_1": "Durum",
        "OSB_ALAN_1": "OSB alanı",
        "PARSEL_S_1": "Parsel sayısı",
        "PARSELIN": "Üretimdeki parsel oranı",
        "PARSEL_DOL": "Tahsis edilen parsel doluluk oranı",
        "ILTISAK_DU": "İltisak hattı durumu",
        "YUKISTASY": "Yük istasyon durumu",
        "ALAN_DOLUL": "Alan doluluğu",
        "ILTISAKDUR": "İltisak hattı durumu",
        "YUKISTDUR": "Yük istasyon durumu",
        "ONCELIK": "Öncelik",
    }

    def props(row):
        raw_status = clean_value(row_by_key(row, column_map, "Fiili_Du_1"))
        status = status_osb(raw_status)
        name = clean_value(row_by_key(row, column_map, "OSB_Ünva_", "OSB_Unva_")) or "OSB"
        city = clean_value(row_by_key(row, column_map, "OSB_İli_1", "OSB_Ili_1"))
        priority = osb_priority(row_by_key(row, column_map, "öncelik", "oncelik"))
        owner = clean_value(row_by_key(row, column_map, "kurum", "Kurum")) or "PLANLANAN ÇALIŞMA YOK"
        details = details_from_columns(row, columns, labels, include_empty=True)
        return {
            "layer": "osb",
            "status": status,
            "rawStatus": raw_status,
            "name": name,
            "city": city,
            "owner": owner,
            "priority": priority["rank"],
            "priorityClass": priority["className"],
            "priorityLabel": priority["label"],
            "details": details,
            "searchText": " ".join([owner, priority["label"], *(item["value"] for item in details)]),
        }

    return point_features(gdf, props)


def logistics_features():
    gdf = read_shp("lojistik_merkezler.shp", encoding="cp1254")
    columns = list(gdf.columns)
    column_map = normalized_columns(gdf)
    labels = {
        "ID_12": "ID",
        "IL_1": "İl",
        "ILCE_1": "İlçe",
        "LOJISTIK_1": "Lojistik merkezi",
        "DURUM_1": "Durum",
        "NOT1": "Not",
        "ACILIS": "Açılış",
        "2024_TAS": "2024 taşıma",
        "2025_DEMIR": "2025 demiryolu",
        "ALAN_M2": "Alan m²",
        "YILLIK_K": "Yıllık kapasite",
        "KURUM": "Kurum",
    }

    def props(row):
        name = clean_value(row_by_key(row, column_map, "Lojistik_1")) or "Lojistik merkezi"
        raw_status = clean_value(row_by_key(row, column_map, "Durum_1"))
        status = status_logistics(raw_status)
        details = details_from_columns(row, columns, labels)
        return {
            "layer": "logistics",
            "status": status,
            "rawStatus": raw_status,
            "name": name,
            "city": clean_value(row_by_key(row, column_map, "İl_1", "Il_1")),
            "district": clean_value(row_by_key(row, column_map, "İlçe_1", "Ilce_1")),
            "details": details,
            "searchText": " ".join(item["value"] for item in details),
        }

    return point_features(gdf, props)


def freight_station_features():
    gdf = read_shp("Yükistasyon*.shp", encoding="cp1254")
    columns = list(gdf.columns)
    labels = {"NO": "No", "ISTASYON_A": "İstasyon adı", "IL": "İl"}

    def props(row):
        name = clean_value(row.get("Istasyon_A")) or "Yük istasyonu"
        details = details_from_columns(row, columns, labels, include_empty=True)
        return {
            "layer": "freightStation",
            "status": "Yük istasyonları",
            "name": name,
            "city": clean_value(row.get("il")),
            "details": details,
            "searchText": " ".join(item["value"] for item in details),
        }

    return point_features(gdf, props)


PROVINCE_LABELS = {
    "SIRA_NO": "Sıra no",
    "IL": "İl",
    "IHRCT_202": "İhracat 2024",
    "PUAN_1": "İhracat puanı",
    "ITHLT_202": "İthalat 2024",
    "PUAN_2": "İthalat puanı",
    "GSYIH_2024": "GSYİH 2024",
    "GSYIH_2025": "GSYİH 2025",
    "PUAN_3": "GSYİH puanı",
    "TURKIYE_G": "Türkiye geneli pay",
    "PUAN_4": "Türkiye geneli puanı",
    "TCDD_DEMIR": "TCDD demiryolu",
    "PUAN_5": "TCDD demiryolu puanı",
    "MEVCUT_OSB": "Mevcut OSB alanı",
    "PUAN_6": "Mevcut OSB puanı",
    "PLAN_OSB_A": "Planlanan OSB alanı",
    "TPLM_OSB_A": "Toplam OSB alanı",
    "PUAN_7": "OSB puanı",
    "IL_ILTISAK": "İl iltisak durumu",
    "PUAN_8": "İltisak puanı",
    "TOPLAM_PUA": "Toplam puan",
}


def province_features():
    gdf = read_source(PROVINCE_SOURCE, encoding="cp1254")
    columns = [column for column in gdf.columns if column != "geometry"]
    normalized_columns = {normalize_key(column): column for column in columns}
    city_column = normalized_columns.get("IL")

    def props(row):
        name = clean_value(row.get(city_column)) if city_column else ""
        details = details_from_pairs(
            [(PROVINCE_LABELS.get(normalize_key(column), clean_value(column)), row.get(column)) for column in columns],
            include_empty=True,
        )
        return {
            "layer": "province",
            "status": "İl bazlı veriler",
            "name": name or "İl",
            "city": name,
            "details": details,
            "searchText": " ".join(item["value"] for item in details),
        }

    return polygon_features(gdf, props, simplify=0.001)


def counts(features):
    result = {}
    for feature in features:
        props = feature["properties"]
        result.setdefault(props["layer"], {})
        result[props["layer"]][props["status"]] = result[props["layer"]].get(props["status"], 0) + 1
    return result


def main():
    province = province_features()
    rail = railway_features()
    connection = connection_features()
    osb = osb_features()
    logistics = logistics_features()
    freight_station = freight_station_features()
    data = {
        "province": feature_collection(province),
        "rail": feature_collection(rail),
        "connection": feature_collection(connection),
        "osb": feature_collection(osb),
        "logistics": feature_collection(logistics),
        "freightStation": feature_collection(freight_station),
        "counts": counts(province + rail + connection + osb + logistics + freight_station),
    }
    for collection_name in ("province", "rail", "connection", "osb", "logistics", "freightStation"):
        for feature in data[collection_name]["features"]:
            feature["geometry"]["coordinates"] = round_coords(feature["geometry"]["coordinates"], 5)
    logo = b64encode((ROOT / "bogazici-proje.jpg").read_bytes()).decode("ascii")
    data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    OUT.write_text(TEMPLATE.replace("__BRAND_LOGO__", logo).replace("__DATA__", data_json), encoding="utf-8")
    print(OUT)
    print(f"province={len(province)} rail={len(rail)} connection={len(connection)} osb={len(osb)} logistics={len(logistics)} freightStation={len(freight_station)}")
    print(f"bytes={OUT.stat().st_size}")


TEMPLATE = r"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>İltisak Çalışması Haritası</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
  <style>
    :root {
      --bg: #f6f3ee;
      --ink: #18221f;
      --muted: #64706d;
      --panel: #fffdf8;
      --line: #d7d1c6;
      --province-fill: #5f89a8;
      --province-line: #4b6174;
      --rail-plan: #111111;
      --rail-project: #111111;
      --rail-current: #111111;
      --connection-planned: #d22b2b;
      --connection-project: #d22b2b;
      --connection-current: #d22b2b;
      --osb-current: #74142c;
      --osb-planned: #d95a58;
      --osb-priority-very-high: #9f1239;
      --osb-priority-high: #e05d2f;
      --osb-priority-medium: #d6a21d;
      --osb-priority-low: #26827a;
      --osb-priority-watch: #6f7780;
      --osb-priority-unknown: #9a9286;
      --logistics-current: #106b37;
      --logistics-planned: #5c8f2a;
      --freight: #8c5a14;
      --shadow: 0 14px 35px rgba(24, 34, 31, .16);
      --poi-scale: .62;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--ink);
      background: var(--bg);
      height: 100vh;
      overflow: hidden;
    }
    .app {
      display: grid;
      grid-template-columns: 360px minmax(0, 1fr);
      grid-template-rows: minmax(0, 1fr);
      height: 100vh;
      height: 100dvh;
      overflow: hidden;
    }
    aside {
      z-index: 600;
      padding: 18px;
      background: var(--panel);
      border-right: 1px solid var(--line);
      box-shadow: var(--shadow);
      min-height: 0;
      overflow-y: auto;
      overflow-x: hidden;
    }
    main {
      display: grid;
      grid-template-rows: minmax(0, 1fr) auto;
      min-width: 0;
      min-height: 0;
      position: relative;
      overflow: hidden;
    }
    #map, #priority-map { height: 100%; width: 100%; background: #dfddd5; }
    .map-view[hidden] { display: none; }
    .map-footer {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 4px 16px;
      padding: 8px 14px;
      border-top: 1px solid var(--line);
      background: var(--panel);
      color: #53615d;
      font-size: 12px;
      line-height: 1.4;
    }
    .brand {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 14px;
      margin-bottom: 16px;
      padding-bottom: 16px;
      border-bottom: 1px solid rgba(215, 209, 198, .9);
    }
    h1 { margin: 0; font-size: 23px; line-height: 1.15; font-weight: 650; letter-spacing: 0; }
    .subtitle { margin: 7px 0 0; color: var(--muted); font-size: 13px; line-height: 1.35; }
    .priority-mode .brand .subtitle { display: none; }
    .brand-logo {
      display: block;
      flex: 0 0 auto;
      align-self: center;
      width: 110px;
      max-width: 36%;
      height: auto;
    }
    .view-switch {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      margin: 0 0 14px;
      padding: 4px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #f7f2e9;
    }
    .view-tab {
      min-width: 0;
      padding: 8px 9px;
      border: 0;
      border-radius: 6px;
      background: transparent;
      color: #53615d;
      font-size: 13px;
      font-weight: 750;
      line-height: 1.15;
    }
    .view-tab.is-active {
      background: #fffefa;
      color: var(--ink);
      box-shadow: 0 1px 0 rgba(255,255,255,.86), 0 6px 14px rgba(24,34,31,.08);
    }
    .view-copy { margin: 0 0 12px; color: var(--muted); font-size: 13px; line-height: 1.35; }
    .sidebar-view[hidden] { display: none; }
    .section {
      padding: 13px 0 0;
    }
    .section h2 {
      margin: 0 0 12px;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: .08em;
      color: #53615d;
      font-weight: 700;
    }
    .section > button#reset-button,
    .section > button#priority-reset-button {
      width: 100%;
      margin-bottom: 8px;
      border-color: #cfc6b8;
      background: linear-gradient(180deg, #fffefa 0%, #f4efe5 100%);
      box-shadow: 0 1px 0 rgba(255,255,255,.8), 0 8px 18px rgba(24,34,31,.06);
    }
    .legend-subtitle {
      margin: 17px 0 7px;
      padding: 8px 10px 6px;
      color: #2d3834;
      font-size: 12px;
      font-weight: 800;
      border-left: 3px solid #2f3d38;
      background: rgba(250, 247, 239, .82);
      border-radius: 0 6px 6px 0;
    }
    .legend-row {
      width: 100%;
      display: grid;
      grid-template-columns: auto 16px minmax(0, 1fr);
      align-items: center;
      gap: 9px;
      padding: 8px 8px;
      color: #2a3431;
      font-size: 14px;
      border: 1px solid transparent;
      border-radius: 6px;
      background: rgba(255,255,255,.42);
      text-align: left;
      cursor: pointer;
    }
    .legend-row:hover, .legend-row.is-active { background: #f4efe5; border-color: #ded6c8; }
    .legend-row.is-hidden { color: #8c9691; }
    .legend-row.is-hidden .swatch, .legend-row.is-hidden .count { opacity: .42; }
    .count { display: none; }
    .visibility-toggle { width: 30px; height: 22px; border: 1px solid #bfc7c3; border-radius: 999px; padding: 2px; background: #fff; position: relative; cursor: pointer; }
    .visibility-toggle::before { content: ""; display: block; width: 16px; height: 16px; border-radius: 50%; background: #23302c; transition: transform .16s ease, background .16s ease; }
    .visibility-toggle[aria-pressed="false"]::before { transform: translateX(8px); background: #a0aaa5; }
    .visibility-toggle[aria-pressed="false"] { background: #f0ede6; }
    .swatch { width: 14px; height: 14px; border-radius: 50%; border: 2px solid #fff; box-shadow: 0 0 0 1px rgba(0,0,0,.15); }
    .swatch.osb { width: 15px; height: 15px; position: relative; display: grid; place-items: center; border-radius: 50%; border: 1px solid rgba(255,255,255,.9); background: var(--osb-swatch) !important; box-shadow: none; color: #fff; font-family: Arial, Helvetica, sans-serif; font-size: 9px; font-weight: 900; line-height: 1; filter: drop-shadow(0 1px 2px rgba(24,34,31,.28)); }
    .swatch.osb::before { content: "O"; transform: translateY(-.2px); }
    .swatch.osb.status-planned { border-style: dashed; }
    .swatch.priority-very-high { background: var(--osb-priority-very-high); }
    .swatch.priority-high { background: var(--osb-priority-high); }
    .swatch.priority-medium { background: var(--osb-priority-medium); }
    .swatch.priority-low { background: var(--osb-priority-low); }
    .swatch.priority-watch { background: var(--osb-priority-watch); }
    .priority-legend .legend-row { grid-template-columns: auto 16px minmax(0, 1fr); cursor: pointer; }
    .priority-legend .legend-row:hover { background: #f4efe5; border-color: #ded6c8; }
    .priority-legend .legend-row.is-hidden { color: #8c9691; }
    .priority-legend .legend-row.is-hidden .swatch { opacity: .35; }
    .institution-key {
      display: grid;
      gap: 6px;
      margin: 9px 0 2px;
      padding: 9px;
      border: 1px solid rgba(215,209,198,.85);
      border-radius: 8px;
      background: rgba(255,255,255,.48);
      color: #3e4a46;
      font-size: 12px;
      line-height: 1.25;
    }
    .institution-key span { display: block; }
    .institution-key strong { display: inline-grid; place-items: center; width: 18px; height: 18px; margin-right: 5px; border-radius: 50%; background: #2d3834; color: #fff; font-size: 11px; }
    .priority-summary {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin: 12px 0 4px;
    }
    .metric {
      padding: 10px;
      border: 1px solid rgba(215,209,198,.9);
      border-radius: 8px;
      background: #fffaf1;
    }
    .metric strong { display: block; font-size: 18px; line-height: 1.1; }
    .metric span { color: var(--muted); font-size: 12px; line-height: 1.2; }
    .swatch.line { height: 4px; border-radius: 99px; border: 0; box-shadow: none; }
    .swatch.line.dashed { background-image: linear-gradient(90deg, currentColor 0 58%, transparent 58% 100%); background-size: 12px 4px; background-color: transparent !important; }
    .swatch.line.dotted { background-image: radial-gradient(circle, currentColor 2px, transparent 2.5px); background-size: 8px 4px; background-color: transparent !important; }
    .swatch.line.rail-construction {
      background: repeating-linear-gradient(90deg, currentColor 0 7px, transparent 7px 12px);
    }
    .swatch.line.rail-project {
      background: radial-gradient(circle at 2px 2px, currentColor 0 2px, transparent 2px);
      background-size: 8px 4px;
    }
    .swatch.triangle { width: 0; height: 0; border-left: 8px solid transparent; border-right: 8px solid transparent; border-bottom: 15px solid var(--triangle-fill); border-top: 0; border-radius: 0; background: transparent !important; box-shadow: none; }
    .swatch.freight { border-radius: 4px; background: var(--freight); transform: rotate(45deg) scale(.8); }
    .swatch.freight::before { content: "Y"; display: grid; place-items: center; color: #fff; font-size: 10px; font-weight: 800; transform: rotate(-45deg); }
    .swatch.province { border-radius: 3px; background: rgba(95,137,168,.22); border-color: rgba(75,97,116,.85); }
    button { border: 1px solid var(--line); border-radius: 7px; padding: 9px 11px; font: inherit; color: var(--ink); background: #fff; cursor: pointer; }
    .category-panel {
      display: grid;
      gap: 9px;
      margin-top: 14px;
      padding: 12px;
      border: 1px solid rgba(215, 209, 198, .92);
      border-radius: 8px;
      background: linear-gradient(180deg, #fffefa 0%, #f7f2e9 100%);
      box-shadow: inset 0 1px 0 rgba(255,255,255,.82), 0 8px 18px rgba(24,34,31,.08);
    }
    .category-panel[hidden] { display: none; }
    .category-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
    .category-head strong { font-size: 14px; line-height: 1.25; letter-spacing: .01em; }
    .category-close { flex: 0 0 auto; padding: 5px 9px; border-radius: 6px; background: #fffaf1; }
    .category-panel input,
    .category-panel select,
    .priority-owner-select { width: 100%; border: 1px solid #cbc4b7; border-radius: 7px; padding: 10px; font: inherit; background: #fff; color: var(--ink); box-shadow: inset 0 1px 2px rgba(24,34,31,.05); }
    .category-note { margin: 0; color: var(--muted); font-size: 12px; line-height: 1.3; }
    .result-list { display: grid; gap: 8px; margin-top: 12px; max-height: 300px; overflow: auto; }
    .result { text-align: left; width: 100%; background: rgba(255,255,255,.74); border-color: #ddd5c8; }
    .result:hover { background: #fff; border-color: #b9afa0; }
    .result small { display: block; margin-top: 3px; color: var(--muted); line-height: 1.25; }
    .leaflet-popup-content-wrapper { border-radius: 8px; box-shadow: var(--shadow); }
    .leaflet-popup-content { width: min(390px, calc(100vw - 58px)) !important; margin: 14px 16px; }
    .popup { width: 100%; max-height: 420px; overflow: auto; padding-right: 2px; }
    .popup h3 { margin: 0 0 7px; font-size: 16px; line-height: 1.22; overflow-wrap: anywhere; }
    .popup .badge { display: inline-flex; margin: 0 0 11px; padding: 4px 8px; border-radius: 999px; background: #f0ece3; color: var(--muted); font-size: 12px; font-weight: 700; line-height: 1.15; }
    .popup dl { display: grid; grid-template-columns: 118px minmax(0, 1fr); gap: 7px 10px; margin: 0; font-size: 13px; line-height: 1.28; }
    .popup dt { color: var(--muted); font-weight: 750; min-width: 0; overflow-wrap: anywhere; }
    .popup dd { margin: 0; min-width: 0; max-width: 100%; white-space: normal; overflow-wrap: anywhere; word-break: break-word; }
    .map-icon { display: block; position: relative; width: 100%; height: 100%; background: var(--marker-fill); border: 2px solid #fff; box-shadow: 0 2px 9px rgba(24, 34, 31, .32); transform: scale(var(--poi-scale)); transform-origin: center; }
    .map-icon.osb {
      display: grid;
      place-items: center;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      border: 1px solid rgba(255,255,255,.9);
      background: var(--marker-fill);
      color: #fff;
      font-family: Arial, Helvetica, sans-serif;
      font-size: 10px;
      font-weight: 900;
      line-height: 1;
      text-shadow: 0 1px 2px rgba(0,0,0,.34);
      box-shadow: none;
      filter: drop-shadow(0 2px 4px rgba(24, 34, 31, .38));
    }
    .map-icon.osb::after { content: "O"; transform: translateY(-.2px); }
    .map-icon.osb.status-planned { border-style: dashed; }
    .priority-marker {
      display: grid;
      place-items: center;
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: var(--marker-fill);
      border: 2px solid #fff;
      color: #fff;
      font-size: 11px;
      font-weight: 900;
      line-height: 1;
      box-shadow: 0 0 0 2px rgba(24,34,31,.18), 0 8px 16px rgba(24,34,31,.34);
    }
    .priority-marker::after { content: attr(data-owner-code); }
    .priority-marker.status-planned { border-style: dashed; }
    .connection-label-card {
      display: none;
      width: 138px;
      transform: rotate(var(--label-angle));
      transform-origin: center;
      padding: 0;
      color: #111;
      font-size: 8px;
      font-weight: 800;
      line-height: 1.08;
      text-align: center;
      white-space: normal;
      pointer-events: none;
      text-shadow:
        -1px -1px 0 #fff,
        1px -1px 0 #fff,
        -1px 1px 0 #fff,
        1px 1px 0 #fff,
        0 0 3px #fff;
    }
    .connection-label-card span { display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .connection-label-card span:first-child { font-weight: 900; color: #111; }
    .show-connection-labels .connection-label-card { display: block; }
    .map-icon.logistics {
      display: grid;
      place-items: center;
      width: 24px;
      height: 24px;
      clip-path: polygon(50% 0, 100% 88%, 0 88%);
      border: 0;
      color: #fff;
      font-size: 12px;
      font-weight: 850;
      line-height: 1;
      box-shadow: none;
      filter: drop-shadow(0 2px 4px rgba(24, 34, 31, .38));
    }
    .map-icon.logistics::before { content: "L"; transform: translateY(3px); }
    .map-icon.freight { display: grid; place-items: center; border-radius: 5px; color: #fff; font-size: 12px; font-weight: 800; line-height: 1; transform: rotate(45deg) scale(var(--poi-scale)); }
    .map-icon.freight::before { content: "Y"; transform: rotate(-45deg); }
    .leaflet-marker-icon { background: transparent; border: 0; }
    .poi-label {
      display: none;
      border: 0;
      border-radius: 4px;
      padding: 2px 5px;
      background: rgba(255, 253, 248, .88);
      box-shadow: 0 1px 4px rgba(24, 34, 31, .16);
      color: #26312d;
      font-size: 10px;
      font-weight: 650;
      line-height: 1.18;
      max-width: 124px;
      white-space: normal;
      overflow-wrap: break-word;
      word-break: normal;
      text-align: left;
      pointer-events: none;
    }
    .show-poi-labels .poi-label { display: block; }
    .priority-label {
      display: none;
      border: 0;
      border-radius: 5px;
      padding: 3px 6px;
      background: rgba(255,253,248,.92);
      box-shadow: 0 2px 8px rgba(24,34,31,.18);
      color: #18221f;
      font-size: 10px;
      font-weight: 750;
      line-height: 1.18;
      max-width: 150px;
      white-space: normal;
      overflow-wrap: break-word;
      pointer-events: none;
    }
    .show-priority-labels .priority-label { display: block; }
    .leaflet-control-layers {
      border: 1px solid rgba(215,209,198,.95) !important;
      border-radius: 8px !important;
      background: rgba(255,253,248,.94) !important;
      box-shadow: 0 12px 26px rgba(24,34,31,.16) !important;
      backdrop-filter: blur(8px);
      color: var(--ink);
      overflow: hidden;
    }
    .leaflet-control-layers-expanded { padding: 10px 12px !important; }
    .leaflet-control-layers-base label {
      display: block;
      padding: 4px 2px;
      font-size: 12px;
      line-height: 1.2;
    }
    .leaflet-control-layers-selector { margin-right: 6px; accent-color: #23302c; }
    @media (max-width: 860px) {
      .app { grid-template-columns: minmax(0, 1fr); grid-template-rows: minmax(0, 47fr) minmax(0, 53fr); }
      aside { border-right: 0; border-bottom: 1px solid var(--line); }
      .map-footer { justify-content: center; text-align: center; }
    }
    @media (max-width: 470px) {
      aside { padding: 14px; }
      .brand { gap: 10px; }
      .brand-logo { width: 96px; }
      .popup dl { grid-template-columns: 1fr; gap: 3px; }
      .popup dd { margin-bottom: 8px; }
    }
  </style>
</head>
<body>
  <div class="app">
    <aside>
      <div class="brand">
        <div>
          <h1>İltisak Çalışması Haritası</h1>
          <p class="subtitle">Demiryolları, iltisak hatları, OSB'ler, lojistik merkezleri ve yük istasyonları için harita arayüzü.</p>
        </div>
        <img class="brand-logo" src="data:image/jpeg;base64,__BRAND_LOGO__" width="600" height="383" alt="Boğaziçi Proje">
      </div>
      <div class="view-switch" role="tablist" aria-label="Harita görünümü">
        <button id="view-explore" class="view-tab is-active" type="button" role="tab" aria-selected="true">İltisak veritabanı</button>
        <button id="view-legend" class="view-tab" type="button" role="tab" aria-selected="false">OSB iltisak önceliklendirme</button>
      </div>
      <div id="database-sidebar" class="sidebar-view">
      <div class="section">
        <h2>Katmanlar</h2>
        <button id="reset-button" type="button">Görünümü sıfırla</button>
        <div class="legend-subtitle">İller</div>
        <button type="button" class="legend-row legend-action" data-explorer="province|İl bazlı veriler|İl bazlı veriler"><span class="visibility-toggle" data-visibility="province|İl bazlı veriler" role="switch" aria-pressed="true" aria-label="İl bazlı veriler görünürlüğü"></span><span class="swatch province"></span><span>İl bazlı veriler</span><span class="count" id="count-province"></span></button>
        <div class="legend-subtitle">Demiryolları</div>
        <button type="button" class="legend-row legend-action rail-legend-row" data-explorer="rail|İnşaat|Demiryolu inşaat"><span class="visibility-toggle" data-visibility="rail|İnşaat" role="switch" aria-pressed="true" aria-label="Demiryolu inşaat görünürlüğü"></span><span class="swatch line rail-construction" style="color:var(--rail-plan)"></span><span>İnşaat</span><span class="count" id="count-rail-construction"></span></button>
        <button type="button" class="legend-row legend-action rail-legend-row" data-explorer="rail|Proje|Demiryolu proje"><span class="visibility-toggle" data-visibility="rail|Proje" role="switch" aria-pressed="true" aria-label="Demiryolu proje görünürlüğü"></span><span class="swatch line rail-project" style="color:var(--rail-project)"></span><span>Proje</span><span class="count" id="count-rail-project"></span></button>
        <button type="button" class="legend-row legend-action rail-legend-row" data-explorer="rail|Mevcut|Demiryolu mevcut"><span class="visibility-toggle" data-visibility="rail|Mevcut" role="switch" aria-pressed="true" aria-label="Demiryolu mevcut görünürlüğü"></span><span class="swatch line" style="background:var(--rail-current)"></span><span>Mevcut</span><span class="count" id="count-rail-current"></span></button>
        <div class="legend-subtitle">İltisak Hatları</div>
        <button type="button" class="legend-row legend-action" data-explorer="connection|Planlanan|İltisak planlanan"><span class="visibility-toggle" data-visibility="connection|Planlanan" role="switch" aria-pressed="true" aria-label="İltisak planlanan görünürlüğü"></span><span class="swatch line dashed" style="color:var(--connection-planned)"></span><span>Planlanan</span><span class="count" id="count-connection-planned"></span></button>
        <button type="button" class="legend-row legend-action" data-explorer="connection|Proje|İltisak proje"><span class="visibility-toggle" data-visibility="connection|Proje" role="switch" aria-pressed="true" aria-label="İltisak proje görünürlüğü"></span><span class="swatch line dotted" style="color:var(--connection-project)"></span><span>Proje</span><span class="count" id="count-connection-project"></span></button>
        <button type="button" class="legend-row legend-action" data-explorer="connection|İnşaat|İltisak inşaat"><span class="visibility-toggle" data-visibility="connection|İnşaat" role="switch" aria-pressed="true" aria-label="İltisak inşaat görünürlüğü"></span><span class="swatch line dashed" style="color:var(--connection-current)"></span><span>İnşaat</span><span class="count" id="count-connection-construction"></span></button>
        <button type="button" class="legend-row legend-action" data-explorer="connection|Yatırım Programında|İltisak yatırım programında"><span class="visibility-toggle" data-visibility="connection|Yatırım Programında" role="switch" aria-pressed="true" aria-label="İltisak yatırım programında görünürlüğü"></span><span class="swatch line dotted" style="color:var(--connection-current)"></span><span>Yatırım Programında</span><span class="count" id="count-connection-investment"></span></button>
        <button type="button" class="legend-row legend-action" data-explorer="connection|Mevcut|İltisak mevcut"><span class="visibility-toggle" data-visibility="connection|Mevcut" role="switch" aria-pressed="true" aria-label="İltisak mevcut görünürlüğü"></span><span class="swatch line" style="background:var(--connection-current)"></span><span>Mevcut</span><span class="count" id="count-connection-current"></span></button>
        <div class="legend-subtitle">OSB</div>
        <button type="button" class="legend-row legend-action" data-explorer="osb|Mevcut|OSB mevcut"><span class="visibility-toggle" data-visibility="osb|Mevcut" role="switch" aria-pressed="true" aria-label="OSB mevcut görünürlüğü"></span><span class="swatch osb" style="--osb-swatch:var(--osb-current)"></span><span>Mevcut</span><span class="count" id="count-osb-current"></span></button>
        <button type="button" class="legend-row legend-action" data-explorer="osb|Planlanan|OSB planlanan"><span class="visibility-toggle" data-visibility="osb|Planlanan" role="switch" aria-pressed="true" aria-label="OSB planlanan görünürlüğü"></span><span class="swatch osb" style="--osb-swatch:var(--osb-planned)"></span><span>Planlanan</span><span class="count" id="count-osb-planned"></span></button>
        <div class="legend-subtitle">Lojistik Odaklar</div>
        <button type="button" class="legend-row legend-action" data-explorer="logistics|Mevcut|Lojistik merkezleri mevcut"><span class="visibility-toggle" data-visibility="logistics|Mevcut" role="switch" aria-pressed="true" aria-label="Lojistik merkezleri mevcut görünürlüğü"></span><span class="swatch triangle" style="--triangle-fill:var(--logistics-current)"></span><span>Lojistik merkezleri mevcut</span><span class="count" id="count-logistics-current"></span></button>
        <button type="button" class="legend-row legend-action" data-explorer="logistics|Planlanan|Lojistik merkezleri planlanan"><span class="visibility-toggle" data-visibility="logistics|Planlanan" role="switch" aria-pressed="true" aria-label="Lojistik merkezleri planlanan görünürlüğü"></span><span class="swatch triangle" style="--triangle-fill:var(--logistics-planned)"></span><span>Lojistik merkezleri planlanan</span><span class="count" id="count-logistics-planned"></span></button>
        <button type="button" class="legend-row legend-action" data-explorer="freightStation|Yük istasyonları|Yük istasyonları"><span class="visibility-toggle" data-visibility="freightStation|Yük istasyonları" role="switch" aria-pressed="true" aria-label="Yük istasyonları görünürlüğü"></span><span class="swatch freight"></span><span>Yük istasyonları</span><span class="count" id="count-freight"></span></button>
        <div id="category-panel" class="category-panel" hidden>
          <div class="category-head">
            <strong id="category-title">Liste</strong>
            <button id="category-close" class="category-close" type="button" aria-label="Listeyi kapat">Kapat</button>
          </div>
          <input id="category-search" type="search" placeholder="Bu kategoride ara">
          <select id="category-owner-filter" aria-label="Kurum filtresi"></select>
          <p id="category-note" class="category-note"></p>
          <div id="category-results" class="result-list" aria-live="polite"></div>
        </div>
      </div>
      </div>
      <div id="priority-sidebar" class="sidebar-view" hidden>
        <div class="section">
          <h2>OSB İltisak Önceliklendirme</h2>
          <button id="priority-reset-button" type="button">Görünümü sıfırla</button>
          <p class="view-copy">Bu harita yalnızca OSB, demiryolu ve iltisak hattı verilerini gösterir. OSB renkleri öncelik sırasına göre sınıflandırılır; 1 en yüksek önceliktir.</p>
          <div class="priority-summary">
            <div class="metric"><strong id="priority-osb-total">0</strong><span>OSB kaydı</span></div>
            <div class="metric"><strong id="priority-connection-total">0</strong><span>İltisak hattı</span></div>
          </div>
          <div class="priority-legend">
            <div class="legend-subtitle">Öncelik Sınıfı</div>
            <button type="button" class="legend-row priority-filter" data-priority-filter="very-high"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch priority-very-high"></span><span>1. Öncelik</span></button>
            <button type="button" class="legend-row priority-filter" data-priority-filter="high"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch priority-high"></span><span>2. Öncelik</span></button>
            <button type="button" class="legend-row priority-filter" data-priority-filter="medium"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch priority-medium"></span><span>3. Öncelik</span></button>
            <button type="button" class="legend-row priority-filter" data-priority-filter="low"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch priority-low"></span><span>4. Öncelik</span></button>
            <button type="button" class="legend-row priority-filter" data-priority-filter="watch"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch priority-watch"></span><span>5. Öncelik</span></button>
            <div class="institution-key" aria-label="Kurum harfleri">
              <span><strong>S</strong>Sanayi Bakanlığı</span>
              <span><strong>A</strong>AYGM</span>
              <span><strong>T</strong>TCDD</span>
            </div>
            <select id="priority-owner-filter" class="priority-owner-select" aria-label="Kurum filtresi"></select>
            <div class="legend-subtitle">Demiryolları</div>
            <button type="button" class="legend-row priority-segment-filter rail-legend-row" data-priority-segment="rail|İnşaat"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch line rail-construction" style="color:var(--rail-plan)"></span><span>İnşaat</span></button>
            <button type="button" class="legend-row priority-segment-filter rail-legend-row" data-priority-segment="rail|Proje"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch line rail-project" style="color:var(--rail-project)"></span><span>Proje</span></button>
            <button type="button" class="legend-row priority-segment-filter rail-legend-row" data-priority-segment="rail|Mevcut"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch line" style="background:var(--rail-current)"></span><span>Mevcut</span></button>
            <div class="legend-subtitle">İltisak Hatları</div>
            <button type="button" class="legend-row priority-segment-filter" data-priority-segment="connection|Planlanan"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch line dashed" style="color:var(--connection-planned)"></span><span>Planlanan</span></button>
            <button type="button" class="legend-row priority-segment-filter" data-priority-segment="connection|Proje"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch line dotted" style="color:var(--connection-project)"></span><span>Proje</span></button>
            <button type="button" class="legend-row priority-segment-filter" data-priority-segment="connection|İnşaat"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch line dashed" style="color:var(--connection-current)"></span><span>İnşaat</span></button>
            <button type="button" class="legend-row priority-segment-filter" data-priority-segment="connection|Yatırım Programında"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch line dotted" style="color:var(--connection-current)"></span><span>Yatırım Programında</span></button>
            <button type="button" class="legend-row priority-segment-filter" data-priority-segment="connection|Mevcut"><span class="visibility-toggle" role="switch" aria-pressed="true"></span><span class="swatch line" style="background:var(--connection-current)"></span><span>Mevcut</span></button>
          </div>
        </div>
      </div>
    </aside>
    <main>
      <div id="map" class="map-view" aria-label="İltisak veritabanı haritası"></div>
      <div id="priority-map" class="map-view" aria-label="OSB iltisak önceliklendirme haritası" hidden></div>
      <footer class="map-footer">
        <span>Bu arayüz Boğaziçi Proje Mühendislik A.Ş. tarafından hazırlanmıştır.</span>
        <span>Copyright © 2026 Boğaziçi Proje Tüm Hakları Saklıdır.</span>
      </footer>
    </main>
  </div>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script>
    const DATA = __DATA__;
    const colors = { provinceFill: "#5f89a8", provinceLine: "#4b6174", railPlan: "#111111", railProject: "#111111", railCurrent: "#111111", connectionPlanned: "#d22b2b", connectionProject: "#d22b2b", connectionCurrent: "#d22b2b", osbCurrent: "#74142c", osbPlanned: "#d95a58", osbPriorityVeryHigh: "#9f1239", osbPriorityHigh: "#e05d2f", osbPriorityMedium: "#d6a21d", osbPriorityLow: "#26827a", osbPriorityWatch: "#6f7780", osbPriorityUnknown: "#9a9286", logisticsCurrent: "#106b37", logisticsPlanned: "#5c8f2a", freight: "#8c5a14", other: "#7254b8" };
    const turkeyBounds = L.latLngBounds([35.55, 25.0], [42.7, 45.3]);
    const map = L.map("map", { preferCanvas: true, zoomControl: true }).setView([39.1, 35.2], 6);
    const esriAttribution = "Tiles &copy; Esri";
    const esri = (service, maxZoom = 19) => L.tileLayer(`https://server.arcgisonline.com/ArcGIS/rest/services/${service}/MapServer/tile/{z}/{y}/{x}`, { maxZoom, attribution: esriAttribution });
    const satelliteWithLabels = L.layerGroup([esri("World_Imagery", 19), esri("Reference/World_Boundaries_and_Places", 19)]);
    const googleSatellite = L.tileLayer("https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", { maxZoom: 20, attribution: "Imagery &copy; Google" });
    const googleHybrid = L.layerGroup([L.tileLayer("https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", { maxZoom: 20, attribution: "Imagery &copy; Google" }), L.tileLayer("https://mt1.google.com/vt/lyrs=h&x={x}&y={y}&z={z}", { maxZoom: 20, attribution: "Labels &copy; Google" })]);
    const baseMaps = {
      "Google Earth Uydu": googleSatellite,
      "Google Earth Hibrit": googleHybrid,
      "Esri Sokak": esri("World_Street_Map", 19),
      "Esri Topo": esri("World_Topo_Map", 19),
      "Esri Gri": esri("Canvas/World_Light_Gray_Base", 16),
      "Esri Uydu": esri("World_Imagery", 19),
      "Esri Uydu + Etiket": satelliteWithLabels,
      "Esri Fiziki": esri("World_Physical_Map", 8),
      "Esri National Geographic": esri("NatGeo_World_Map", 16),
      "OpenStreetMap": L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", { maxZoom: 19, attribution: '&copy; OpenStreetMap' }),
      "Carto Voyager": L.tileLayer("https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png", { maxZoom: 20, attribution: '&copy; OpenStreetMap &copy; CARTO' })
    };
    baseMaps["Google Earth Uydu"].addTo(map);
    const panes = { province: map.createPane("province-pane"), rail: map.createPane("rail-pane"), connection: map.createPane("connection-pane"), connectionLabel: map.createPane("connection-label-pane"), osb: map.createPane("osb-pane"), logistics: map.createPane("logistics-pane"), freightStation: map.createPane("freight-pane") };
    panes.province.style.zIndex = 360; panes.rail.style.zIndex = 410; panes.connection.style.zIndex = 425; panes.connectionLabel.style.zIndex = 432; panes.osb.style.zIndex = 435; panes.logistics.style.zIndex = 445; panes.freightStation.style.zIndex = 450;
    panes.connectionLabel.style.pointerEvents = "none";
    const railRenderer = L.canvas({ pane: "rail-pane", tolerance: 10 });
    const connectionRenderer = L.canvas({ pane: "connection-pane", tolerance: 12 });
    const clickPopup = L.popup({ maxWidth: 380 });
    let directFeatureClick = false;
    let activeCategory = null;
    let currentView = "explore";

    function escapeHtml(value) { return String(value).replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" })[char]); }
    function layerLabel(layer) { return ({ province: "İl bazlı veriler", rail: "Demiryolu", connection: "İltisak hattı", osb: "OSB", logistics: "Lojistik merkezi", freightStation: "Yük istasyonu" })[layer] || layer; }
    function detailValue(props, label) { const item = (props.details || []).find(row => row.label === label); return item?.value || ""; }
    function propertyRows(props) { return (props.details || []).map(item => `<dt>${escapeHtml(item.label)}</dt><dd>${escapeHtml(item.value)}</dd>`).join(""); }
    function popupHtml(props) { const badge = [layerLabel(props.layer), props.rawStatus || props.status].filter(Boolean).join(" · "); return `<div class="popup"><h3>${escapeHtml(props.name || "Kayıt")}</h3><span class="badge">${escapeHtml(badge)}</span><dl>${propertyRows(props)}</dl></div>`; }
    function bindFeaturePopup(feature, layer) { layer.bindPopup(popupHtml(feature.properties)); layer.on("click", (event) => { directFeatureClick = true; if (event?.latlng) layer.openPopup(event.latlng); else layer.openPopup(); }); }
    function provinceStyle() { return { pane: "province-pane", color: colors.provinceLine, weight: 1.35, opacity: 0.78, fillColor: colors.provinceFill, fillOpacity: 0.09 }; }
    function railStyle(feature) {
      const status = feature.properties.status;
      const color = status === "Mevcut" ? colors.railCurrent : status === "Proje" ? colors.railProject : status === "İnşaat" ? colors.railPlan : colors.other;
      return {
        pane: "rail-pane",
        color,
        weight: status === "Mevcut" ? 3 : status === "Proje" ? 4.5 : 4,
        opacity: status === "Mevcut" ? 0.9 : 0.96,
        dashArray: status === "Mevcut" ? null : status === "İnşaat" ? "20 10" : "1 9",
        lineCap: status === "Proje" ? "round" : "butt",
      };
    }
    function connectionStyle(feature) { const status = feature.properties.status; const color = status === "Mevcut" ? colors.connectionCurrent : status === "Proje" ? colors.connectionProject : status === "Planlanan" ? colors.connectionPlanned : colors.connectionCurrent; const dashArray = status === "Mevcut" ? null : status === "Planlanan" ? "12 6" : status === "Proje" ? "3 7" : status === "İnşaat" ? "8 4 2 4" : "2 6"; return { pane: "connection-pane", color, weight: 5, opacity: 0.96, dashArray, lineCap: "round" }; }
    function pointIcon(feature) {
      const layer = feature.properties.layer;
      if (layer === "freightStation") return L.divIcon({ className: "", html: `<span class="map-icon freight" style="--marker-fill:${colors.freight}"></span>`, iconSize: [18, 18], iconAnchor: [9, 9], popupAnchor: [0, -10] });
      if (layer === "logistics") {
        const fill = feature.properties.status === "Mevcut" ? colors.logisticsCurrent : colors.logisticsPlanned;
        return L.divIcon({ className: "", html: `<span class="map-icon logistics" style="--marker-fill:${fill}"></span>`, iconSize: [24, 24], iconAnchor: [12, 20], popupAnchor: [0, -13] });
      }
      const fill = feature.properties.status === "Mevcut" ? colors.osbCurrent : colors.osbPlanned;
      return L.divIcon({ className: "", html: `<span class="map-icon osb" style="--marker-fill:${fill}"></span>`, iconSize: [18, 18], iconAnchor: [9, 9], popupAnchor: [0, -10] });
    }

    const provinceLayer = L.geoJSON(DATA.province, { pane: "province-pane", style: provinceStyle, onEachFeature: bindFeaturePopup });
    const railLayer = L.geoJSON(DATA.rail, { pane: "rail-pane", renderer: railRenderer, style: railStyle, onEachFeature: bindFeaturePopup });
    const connectionLayer = L.geoJSON(DATA.connection, { pane: "connection-pane", renderer: connectionRenderer, style: connectionStyle, onEachFeature: bindFeaturePopup });
    const connectionLabelLayer = L.layerGroup().addTo(map);
    const connectionLabelItems = [];
    function connectionLabelData(feature) {
      let best = null;
      walkLineSegments(feature.geometry.coordinates, (start, end) => {
        const a = map.latLngToLayerPoint([start[1], start[0]]);
        const b = map.latLngToLayerPoint([end[1], end[0]]);
        const length = a.distanceTo(b);
        if (!best || length > best.length) {
          let angle = Math.atan2(b.y - a.y, b.x - a.x) * 180 / Math.PI;
          if (angle > 90 || angle < -90) angle += 180;
          best = { length, angle, latlng: L.latLng((start[1] + end[1]) / 2, (start[0] + end[0]) / 2) };
        }
      });
      return best;
    }
    function connectionLabelIcon(feature, angle) {
      const props = feature.properties;
      const owner = detailValue(props, "Kurum") || "Kurum yok";
      const html = `<div class="connection-label-card" style="--label-angle:${angle}deg"><span>${escapeHtml(props.name || "İltisak hattı")}</span><span>${escapeHtml(props.status || "")}</span><span>${escapeHtml(owner)}</span></div>`;
      return L.divIcon({ className: "", html, iconSize: [138, 32], iconAnchor: [69, 16] });
    }
    function makeConnectionLabel(feature) {
      const data = connectionLabelData(feature);
      if (!data) return;
      const marker = L.marker(data.latlng, { pane: "connection-label-pane", interactive: false, icon: connectionLabelIcon(feature, data.angle) });
      marker.addTo(connectionLabelLayer);
      connectionLabelItems.push({ feature, marker });
    }
    DATA.connection.features.forEach(makeConnectionLabel);
    function pointMarker(feature, latlng, pane) {
      return L.marker(latlng, { pane, icon: pointIcon(feature) })
        .bindTooltip(feature.properties.name || "", {
          permanent: true,
          direction: "right",
          offset: [10, 0],
          className: "poi-label"
        });
    }

    const osbLayer = L.geoJSON(DATA.osb, { pointToLayer: (feature, latlng) => pointMarker(feature, latlng, "osb-pane"), onEachFeature: bindFeaturePopup });
    const logisticsLayer = L.geoJSON(DATA.logistics, { pointToLayer: (feature, latlng) => pointMarker(feature, latlng, "logistics-pane"), onEachFeature: bindFeaturePopup });
    const freightStationLayer = L.geoJSON(DATA.freightStation, { pointToLayer: (feature, latlng) => pointMarker(feature, latlng, "freight-pane"), onEachFeature: bindFeaturePopup });
    const layerMap = { province: provinceLayer, rail: railLayer, connection: connectionLayer, osb: osbLayer, logistics: logisticsLayer, freightStation: freightStationLayer };
    Object.values(layerMap).forEach(layer => layer.addTo(map));
    L.control.layers(baseMaps, null, { collapsed: false }).addTo(map);
    map.fitBounds(turkeyBounds, { padding: [12, 12] });
    let visibleSegments;
    function updatePoiScale() { const zoom = map.getZoom(); const scale = zoom <= 6 ? .56 : zoom === 7 ? .72 : zoom === 8 ? .88 : zoom >= 11 ? 1.18 : 1; document.documentElement.style.setProperty("--poi-scale", scale); const showLabels = currentView === "explore"; map.getContainer().classList.toggle("show-poi-labels", showLabels && zoom >= 10); map.getContainer().classList.toggle("show-connection-labels", showLabels && zoom >= 11); updateConnectionLabelPositions(); }
    map.on("zoomend moveend", updatePoiScale); updatePoiScale();

    function segmentKey(layer, status) { return `${layer}|${status}`; }
    const segmentLayerItems = new Map();
    Object.values(layerMap).forEach(parentLayer => { parentLayer.eachLayer(item => { const props = item.feature?.properties; if (!props) return; const key = segmentKey(props.layer, props.status); if (!segmentLayerItems.has(key)) segmentLayerItems.set(key, []); segmentLayerItems.get(key).push({ parentLayer, item }); }); });
    visibleSegments = new Map(Array.from(segmentLayerItems.keys()).map(key => [key, true]));
    function updateVisibilityToggle(layer, status, visible) { const key = segmentKey(layer, status); document.querySelectorAll("[data-visibility]").forEach(toggle => { if (toggle.dataset.visibility !== key) return; toggle.setAttribute("aria-pressed", visible ? "true" : "false"); toggle.closest(".legend-row")?.classList.toggle("is-hidden", !visible); }); }
    function setSegmentVisibility(layer, status, visible) { const key = segmentKey(layer, status); visibleSegments.set(key, visible); (segmentLayerItems.get(key) || []).forEach(({ parentLayer, item }) => { if (visible && !parentLayer.hasLayer(item)) parentLayer.addLayer(item); if (!visible && parentLayer.hasLayer(item)) parentLayer.removeLayer(item); }); updateVisibilityToggle(layer, status, visible); updateConnectionLabelVisibility(); }
    function isSegmentVisible(layer, status) { return !visibleSegments || visibleSegments.get(segmentKey(layer, status)) !== false; }
    function updateConnectionLabelPositions() { connectionLabelItems.forEach(({ feature, marker }) => { const data = connectionLabelData(feature); if (!data) return; marker.setLatLng(data.latlng); marker.setIcon(connectionLabelIcon(feature, data.angle)); }); updateConnectionLabelVisibility(); }
    function updateConnectionLabelVisibility() { connectionLabelItems.forEach(({ feature, marker }) => { const props = feature.properties; const visible = map.hasLayer(connectionLayer) && isSegmentVisible(props.layer, props.status); if (visible && !connectionLabelLayer.hasLayer(marker)) marker.addTo(connectionLabelLayer); if (!visible && connectionLabelLayer.hasLayer(marker)) connectionLabelLayer.removeLayer(marker); }); }
    function setText(id, value) { const el = document.getElementById(id); if (el) el.textContent = Number(value || 0).toLocaleString("tr-TR"); }
    setText("count-province", DATA.counts.province?.["İl bazlı veriler"]); setText("count-rail-construction", DATA.counts.rail?.["İnşaat"]); setText("count-rail-project", DATA.counts.rail?.Proje); setText("count-rail-current", DATA.counts.rail?.Mevcut);
    setText("count-connection-planned", DATA.counts.connection?.Planlanan); setText("count-connection-project", DATA.counts.connection?.Proje); setText("count-connection-construction", DATA.counts.connection?.["İnşaat"]); setText("count-connection-investment", DATA.counts.connection?.["Yatırım Programında"]); setText("count-connection-current", DATA.counts.connection?.Mevcut);
    setText("count-osb-current", DATA.counts.osb?.Mevcut); setText("count-osb-planned", DATA.counts.osb?.Planlanan); setText("count-logistics-current", DATA.counts.logistics?.Mevcut); setText("count-logistics-planned", DATA.counts.logistics?.Planlanan); setText("count-freight", DATA.counts.freightStation?.["Yük istasyonları"]);
    document.querySelectorAll("[data-visibility]").forEach(toggle => { const [layer, status] = toggle.dataset.visibility.split("|"); updateVisibilityToggle(layer, status, isSegmentVisible(layer, status)); toggle.addEventListener("click", event => { event.preventDefault(); event.stopPropagation(); setSegmentVisibility(layer, status, !isSegmentVisible(layer, status)); }); });
    function closeCategoryPanel() { activeCategory = null; document.getElementById("category-panel").hidden = true; document.querySelectorAll(".legend-action").forEach(button => button.classList.remove("is-active")); }

    const priorityMap = L.map("priority-map", { preferCanvas: true, zoomControl: true }).setView([39.1, 35.2], 6);
    const prioritySatelliteWithLabels = L.layerGroup([esri("World_Imagery", 19), esri("Reference/World_Boundaries_and_Places", 19)]);
    const priorityGoogleSatellite = L.tileLayer("https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", { maxZoom: 20, attribution: "Imagery &copy; Google" });
    const priorityGoogleHybrid = L.layerGroup([L.tileLayer("https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", { maxZoom: 20, attribution: "Imagery &copy; Google" }), L.tileLayer("https://mt1.google.com/vt/lyrs=h&x={x}&y={y}&z={z}", { maxZoom: 20, attribution: "Labels &copy; Google" })]);
    const priorityBaseMaps = {
      "Google Earth Uydu": priorityGoogleSatellite,
      "Google Earth Hibrit": priorityGoogleHybrid,
      "Esri Sokak": esri("World_Street_Map", 19),
      "Esri Topo": esri("World_Topo_Map", 19),
      "Esri Gri": esri("Canvas/World_Light_Gray_Base", 16),
      "Esri Uydu": esri("World_Imagery", 19),
      "Esri Uydu + Etiket": prioritySatelliteWithLabels,
      "Esri Fiziki": esri("World_Physical_Map", 8),
      "Esri National Geographic": esri("NatGeo_World_Map", 16),
      "OpenStreetMap": L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", { maxZoom: 19, attribution: '&copy; OpenStreetMap' }),
      "Carto Voyager": L.tileLayer("https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png", { maxZoom: 20, attribution: '&copy; OpenStreetMap &copy; CARTO' })
    };
    priorityBaseMaps["Google Earth Uydu"].addTo(priorityMap);
    L.control.layers(priorityBaseMaps, null, { collapsed: false }).addTo(priorityMap);
    const priorityPanes = { rail: priorityMap.createPane("priority-rail-pane"), connection: priorityMap.createPane("priority-connection-pane"), osb: priorityMap.createPane("priority-osb-pane") };
    priorityPanes.rail.style.zIndex = 410; priorityPanes.connection.style.zIndex = 430; priorityPanes.osb.style.zIndex = 460;
    const priorityRailRenderer = L.canvas({ pane: "priority-rail-pane", tolerance: 10 });
    const priorityConnectionRenderer = L.canvas({ pane: "priority-connection-pane", tolerance: 12 });
    const priorityColors = { "very-high": colors.osbPriorityVeryHigh, high: colors.osbPriorityHigh, medium: colors.osbPriorityMedium, low: colors.osbPriorityLow, watch: colors.osbPriorityWatch, unknown: colors.osbPriorityUnknown };
    function priorityRailStyle(feature) { const base = railStyle(feature); return { ...base, pane: "priority-rail-pane", opacity: .72, weight: base.weight + .5 }; }
    function priorityConnectionStyle(feature) { const base = connectionStyle(feature); return { ...base, pane: "priority-connection-pane", opacity: .98, weight: 6 }; }
    function ownerCode(owner) {
      const key = String(owner || "").toLocaleUpperCase("tr-TR");
      if (key.includes("SANAYİ") || key.includes("SANAYI")) return "S";
      if (key.includes("AYGM")) return "A";
      if (key.includes("TCDD")) return "T";
      return "";
    }
    function priorityOsbIcon(feature) {
      const fill = priorityColors[feature.properties.priorityClass] || colors.osbPriorityUnknown;
      const size = feature.properties.priorityClass === "very-high" ? 24 : feature.properties.priorityClass === "high" ? 21 : feature.properties.priorityClass === "medium" ? 18 : 16;
      const statusClass = feature.properties.status === "Planlanan" ? " status-planned" : "";
      const code = ownerCode(feature.properties.owner);
      return L.divIcon({ className: "", html: `<span class="priority-marker${statusClass}" data-owner-code="${escapeHtml(code)}" style="--marker-fill:${fill}"></span>`, iconSize: [size, size], iconAnchor: [size / 2, size / 2], popupAnchor: [0, -size / 2] });
    }
    function priorityPopupHtml(props) {
      const rows = [
        ["Öncelik", props.priority || "-"],
        ["Sınıf", props.priorityLabel || "-"],
        ["Kurum", props.owner || "-"],
        ["Durum", props.rawStatus || props.status || "-"],
        ["İl", props.city || "-"]
      ].map(([label, value]) => `<dt>${escapeHtml(label)}</dt><dd>${escapeHtml(value)}</dd>`).join("");
      return `<div class="popup"><h3>${escapeHtml(props.name || "OSB")}</h3><span class="badge">${escapeHtml(props.priorityLabel || "Öncelik")}</span><dl>${rows}</dl></div>`;
    }
    function bindPriorityPopup(feature, layer) { layer.bindPopup(priorityPopupHtml(feature.properties)); }
    const priorityRailLayer = L.geoJSON(DATA.rail, { pane: "priority-rail-pane", renderer: priorityRailRenderer, style: priorityRailStyle, onEachFeature: bindFeaturePopup }).addTo(priorityMap);
    const priorityConnectionLayer = L.geoJSON(DATA.connection, { pane: "priority-connection-pane", renderer: priorityConnectionRenderer, style: priorityConnectionStyle, onEachFeature: bindFeaturePopup }).addTo(priorityMap);
    const priorityOsbLayer = L.geoJSON(DATA.osb, { pointToLayer: (feature, latlng) => L.marker(latlng, { pane: "priority-osb-pane", icon: priorityOsbIcon(feature) }), onEachFeature: bindPriorityPopup }).addTo(priorityMap);
    priorityOsbLayer.eachLayer(marker => {
      const props = marker.feature?.properties || {};
      marker.bindTooltip(`${props.name || "OSB"} · ${props.priorityLabel || ""}`, {
        permanent: true,
        direction: "right",
        offset: [12, 0],
        className: "priority-label"
      });
    });
    const priorityClassItems = new Map();
    priorityOsbLayer.eachLayer(marker => {
      const className = marker.feature?.properties?.priorityClass || "unknown";
      if (!priorityClassItems.has(className)) priorityClassItems.set(className, []);
      priorityClassItems.get(className).push(marker);
    });
    const visiblePriorityClasses = new Map(Array.from(priorityClassItems.keys()).map(key => [key, true]));
    function sortOwners(owners) { return owners.sort((a, b) => { const emptyA = a === "PLANLANAN ÇALIŞMA YOK"; const emptyB = b === "PLANLANAN ÇALIŞMA YOK"; if (emptyA !== emptyB) return emptyA ? 1 : -1; return a.localeCompare(b, "tr"); }); }
    const priorityOwners = sortOwners(Array.from(new Set([...DATA.osb.features, ...DATA.connection.features].map(feature => feature.properties.owner || "PLANLANAN ÇALIŞMA YOK"))));
    const priorityOwnerFilter = document.getElementById("priority-owner-filter");
    priorityOwnerFilter.innerHTML = `<option value="">Tüm kurumlar</option>${priorityOwners.map(owner => `<option value="${escapeHtml(owner)}">${escapeHtml(owner)}</option>`).join("")}`;
    function ownerVisible(owner) { return !priorityOwnerFilter.value || (owner || "PLANLANAN ÇALIŞMA YOK") === priorityOwnerFilter.value; }
    function refreshPriorityOsbVisibility() {
      priorityClassItems.forEach(markers => {
        markers.forEach(marker => {
          const props = marker.feature?.properties || {};
          const visible = visiblePriorityClasses.get(props.priorityClass || "unknown") !== false && ownerVisible(props.owner);
          if (visible && !priorityOsbLayer.hasLayer(marker)) priorityOsbLayer.addLayer(marker);
          if (!visible && priorityOsbLayer.hasLayer(marker)) priorityOsbLayer.removeLayer(marker);
        });
      });
    }
    function setPriorityClassVisible(className, visible) {
      visiblePriorityClasses.set(className, visible);
      refreshPriorityOsbVisibility();
      document.querySelectorAll(`[data-priority-filter="${className}"]`).forEach(button => {
        button.classList.toggle("is-hidden", !visible);
        button.setAttribute("aria-pressed", visible ? "true" : "false");
        button.querySelector(".visibility-toggle")?.setAttribute("aria-pressed", visible ? "true" : "false");
      });
    }
    document.querySelectorAll("[data-priority-filter]").forEach(button => {
      const className = button.dataset.priorityFilter;
      button.setAttribute("aria-pressed", "true");
      button.addEventListener("click", () => setPriorityClassVisible(className, visiblePriorityClasses.get(className) === false));
    });
    const prioritySegmentItems = new Map();
    [priorityRailLayer, priorityConnectionLayer].forEach(parentLayer => {
      parentLayer.eachLayer(item => {
        const props = item.feature?.properties;
        if (!props) return;
        const key = segmentKey(props.layer, props.status);
        if (!prioritySegmentItems.has(key)) prioritySegmentItems.set(key, []);
        prioritySegmentItems.get(key).push({ parentLayer, item });
      });
    });
    const visiblePrioritySegments = new Map(Array.from(prioritySegmentItems.keys()).map(key => [key, true]));
    function refreshPrioritySegmentVisibility() {
      prioritySegmentItems.forEach((items, key) => {
        items.forEach(({ parentLayer, item }) => {
          const props = item.feature?.properties || {};
          const visible = visiblePrioritySegments.get(key) !== false && (props.layer !== "connection" || ownerVisible(props.owner));
          if (visible && !parentLayer.hasLayer(item)) parentLayer.addLayer(item);
          if (!visible && parentLayer.hasLayer(item)) parentLayer.removeLayer(item);
        });
      });
    }
    function setPrioritySegmentVisible(key, visible) {
      visiblePrioritySegments.set(key, visible);
      refreshPrioritySegmentVisibility();
      document.querySelectorAll(`[data-priority-segment="${key}"]`).forEach(button => {
        button.classList.toggle("is-hidden", !visible);
        button.setAttribute("aria-pressed", visible ? "true" : "false");
        button.querySelector(".visibility-toggle")?.setAttribute("aria-pressed", visible ? "true" : "false");
      });
    }
    document.querySelectorAll("[data-priority-segment]").forEach(button => {
      const key = button.dataset.prioritySegment;
      button.setAttribute("aria-pressed", "true");
      button.addEventListener("click", () => setPrioritySegmentVisible(key, visiblePrioritySegments.get(key) === false));
    });
    function applyPriorityOwnerFilter() {
      refreshPriorityOsbVisibility();
      refreshPrioritySegmentVisibility();
    }
    priorityOwnerFilter.addEventListener("change", applyPriorityOwnerFilter);
    function resetPriorityMap() { priorityMap.fitBounds(turkeyBounds, { padding: [12, 12] }); }
    function updatePriorityLabels() { priorityMap.getContainer().classList.toggle("show-priority-labels", priorityMap.getZoom() >= 10); }
    priorityMap.on("zoomend", updatePriorityLabels);
    setText("priority-osb-total", DATA.osb.features.length);
    setText("priority-connection-total", DATA.connection.features.length);

    function setViewMode(view) {
      currentView = view;
      document.body.classList.toggle("priority-mode", view === "legend");
      document.getElementById("view-explore").classList.toggle("is-active", view === "explore");
      document.getElementById("view-legend").classList.toggle("is-active", view === "legend");
      document.getElementById("view-explore").setAttribute("aria-selected", view === "explore" ? "true" : "false");
      document.getElementById("view-legend").setAttribute("aria-selected", view === "legend" ? "true" : "false");
      document.getElementById("database-sidebar").hidden = view !== "explore";
      document.getElementById("priority-sidebar").hidden = view !== "legend";
      document.getElementById("map").hidden = view !== "explore";
      document.getElementById("priority-map").hidden = view !== "legend";
      if (view === "legend") {
        closeCategoryPanel();
        setTimeout(() => { priorityMap.invalidateSize(); resetPriorityMap(); updatePriorityLabels(); }, 0);
      } else {
        setTimeout(() => map.invalidateSize(), 0);
      }
      updatePoiScale();
    }
    document.getElementById("view-explore").addEventListener("click", () => setViewMode("explore"));
    document.getElementById("view-legend").addEventListener("click", () => setViewMode("legend"));
    document.getElementById("priority-reset-button").addEventListener("click", resetPriorityMap);

    function allSearchableFeatures() { return [...DATA.province.features, ...DATA.rail.features, ...DATA.connection.features, ...DATA.osb.features, ...DATA.logistics.features, ...DATA.freightStation.features]; }
    function searchableText(feature) { const props = feature.properties; return [props.name, props.city, props.district, props.owner, props.rawStatus, props.status, props.searchText].filter(Boolean).join(" ").toLocaleLowerCase("tr-TR"); }
    function entrySearchText(entry) { return entry.features.map(searchableText).join(" "); }
    function categoryEntries(layer, status) { const groups = new Map(); for (const feature of allSearchableFeatures()) { const props = feature.properties; if (props.layer !== layer || props.status !== status) continue; const name = props.name || "Kayıt"; const owner = props.owner || "PLANLANAN ÇALIŞMA YOK"; const key = `${layer}|${status}|${owner}|${name.toLocaleLowerCase("tr-TR")}`; if (!groups.has(key)) groups.set(key, { feature, features: [], name, owner }); groups.get(key).features.push(feature); } return Array.from(groups.values()).sort((a, b) => a.name.localeCompare(b.name, "tr")); }
    function updateCategoryOwnerFilter() { const select = document.getElementById("category-owner-filter"); if (!activeCategory) return; const owners = sortOwners(Array.from(new Set(categoryEntries(activeCategory.layer, activeCategory.status).map(entry => entry.owner || "PLANLANAN ÇALIŞMA YOK")))); select.innerHTML = `<option value="">Tüm kurumlar</option>${owners.map(owner => `<option value="${escapeHtml(owner)}">${escapeHtml(owner)}</option>`).join("")}`; select.hidden = owners.length <= 1; }
    function openCategory(layer, status, title, sourceButton) { if (currentView === "legend") return; activeCategory = { layer, status, title }; document.querySelectorAll(".legend-action").forEach(button => button.classList.remove("is-active")); if (sourceButton) sourceButton.classList.add("is-active"); document.getElementById("category-panel").hidden = false; document.getElementById("category-title").textContent = title; const search = document.getElementById("category-search"); search.value = ""; search.placeholder = `${title} içinde ara`; updateCategoryOwnerFilter(); renderCategoryResults(); search.focus(); }
    function renderCategoryResults() { const results = document.getElementById("category-results"); const note = document.getElementById("category-note"); results.innerHTML = ""; if (!activeCategory) return; const q = document.getElementById("category-search").value.trim().toLocaleLowerCase("tr-TR"); const ownerFilter = document.getElementById("category-owner-filter").value; const all = categoryEntries(activeCategory.layer, activeCategory.status); const byOwner = ownerFilter ? all.filter(entry => entry.owner === ownerFilter) : all; const filtered = q ? byOwner.filter(entry => entrySearchText(entry).includes(q)) : byOwner; const visible = filtered.slice(0, 250); const segmentTotal = filtered.reduce((sum, entry) => sum + entry.features.length, 0); note.textContent = `${filtered.length.toLocaleString("tr-TR")} tekil kayıt, ${segmentTotal.toLocaleString("tr-TR")} parça${filtered.length > visible.length ? " - ilk 250 gösteriliyor, aramayı daraltın" : ""}`; if (!visible.length) { results.innerHTML = '<div class="subtitle">Sonuç bulunamadı.</div>'; return; } for (const entry of visible) { const feature = entry.feature; const props = feature.properties; const button = document.createElement("button"); button.type = "button"; button.className = "result"; const detail = [layerLabel(props.layer), props.owner, props.city, props.district, props.rawStatus || props.status].filter(Boolean).join(" · "); const segmentInfo = entry.features.length > 1 ? ` · ${entry.features.length.toLocaleString("tr-TR")} parça` : ""; button.innerHTML = `${escapeHtml(props.name || "Kayıt")}<small>${escapeHtml(detail)}${segmentInfo}</small>`; button.addEventListener("click", () => focusEntry(entry)); results.appendChild(button); } }
    document.querySelectorAll(".legend-action[data-explorer]").forEach(button => { button.addEventListener("click", () => { const [layer, status, title] = button.dataset.explorer.split("|"); openCategory(layer, status, title, button); }); });
    document.getElementById("category-search").addEventListener("input", renderCategoryResults);
    document.getElementById("category-owner-filter").addEventListener("change", renderCategoryResults);
    document.getElementById("category-close").addEventListener("click", closeCategoryPanel);
    function distanceToSegment(point, a, b) { const dx = b.x - a.x; const dy = b.y - a.y; if (dx === 0 && dy === 0) return point.distanceTo(a); const t = Math.max(0, Math.min(1, ((point.x - a.x) * dx + (point.y - a.y) * dy) / (dx * dx + dy * dy))); return point.distanceTo(L.point(a.x + t * dx, a.y + t * dy)); }
    function walkLineSegments(coords, visit) { if (!coords?.length) return; if (typeof coords[0][0] === "number") { for (let i = 1; i < coords.length; i++) visit(coords[i - 1], coords[i]); } else { coords.forEach(part => walkLineSegments(part, visit)); } }
    function distanceToLineFeature(event, feature) { let best = Infinity; const clickPoint = map.latLngToLayerPoint(event.latlng); walkLineSegments(feature.geometry.coordinates, (start, end) => { const a = map.latLngToLayerPoint([start[1], start[0]]); const b = map.latLngToLayerPoint([end[1], end[0]]); best = Math.min(best, distanceToSegment(clickPoint, a, b)); }); return best; }
    function openFallbackPopup(feature, latlng) { if (!feature) return false; clickPopup.setLatLng(latlng).setContent(popupHtml(feature.properties)).openOn(map); return true; }
    function fallbackMapClick(event) { if (directFeatureClick) { directFeatureClick = false; return; } const lineSources = []; if (map.hasLayer(railLayer)) lineSources.push(...DATA.rail.features.filter(feature => isSegmentVisible(feature.properties.layer, feature.properties.status))); if (map.hasLayer(connectionLayer)) lineSources.push(...DATA.connection.features.filter(feature => isSegmentVisible(feature.properties.layer, feature.properties.status))); let nearest = null; let nearestDistance = Infinity; for (const feature of lineSources) { const distance = distanceToLineFeature(event, feature); if (distance < nearestDistance) { nearestDistance = distance; nearest = feature; } } if (nearestDistance <= 14) openFallbackPopup(nearest, event.latlng); }
    map.on("click", fallbackMapClick);
    function focusEntry(entry) { const feature = entry.feature; const layer = layerMap[feature.properties.layer]; if (!map.hasLayer(layer)) layer.addTo(map); if (!isSegmentVisible(feature.properties.layer, feature.properties.status)) setSegmentVisibility(feature.properties.layer, feature.properties.status, true); const temp = L.geoJSON(entry.features); const bounds = temp.getBounds(); if (feature.geometry.type === "Point") { const [lng, lat] = feature.geometry.coordinates; map.setView([lat, lng], Math.max(map.getZoom(), 11), { animate: true }); } else { map.fitBounds(bounds.pad(0.25), { animate: true, maxZoom: 11 }); } let targetLayer = null; layer.eachLayer(item => { if (targetLayer) return; const p = item.feature?.properties; if (p && p.name === feature.properties.name && p.status === feature.properties.status) targetLayer = item; }); if (targetLayer) targetLayer.openPopup(); }
    document.getElementById("reset-button").addEventListener("click", () => map.fitBounds(turkeyBounds, { padding: [12, 12] }));
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    main()


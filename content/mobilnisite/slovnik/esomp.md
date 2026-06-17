---
slug: "esomp"
url: "/mobilnisite/slovnik/esomp/"
type: "slovnik"
title: "ESOMP – Earth Stations on Mobile Platforms"
date: 2025-01-01
abbr: "ESOMP"
fullName: "Earth Stations on Mobile Platforms"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/esomp/"
summary: "Earth Stations on Mobile Platforms (ESOMP) jsou satelitní komunikační terminály instalované na pohybujících se vozidlech, jako jsou letadla, lodě a vlaky. Umožňují širokopásmové připojení pro cestujíc"
---

ESOMP je satelitní komunikační terminál instalovaný na pohybujících se vozidlech, jako jsou letadla, lodě a vlaky, který poskytuje širokopásmové připojení tím, že propojuje platformu přímo se satelity, čímž rozšiřuje pokrytí mimo pozemní sítě.

## Popis

Earth Stations on Mobile Platforms (ESOMP) označují třídu satelitní uživatelské stanice definovanou 3GPP pro poskytování komunikačních služeb pohybujícím se platformám. ESOMP je v podstatě satelitní terminál – skládající se z antény, rádiového transceiveru a příslušných řídicích systémů – instalovaný na vozidle, jako je letadlo (ESOA), loď (ESVS) nebo vlak. Jeho hlavní funkcí je vytvoření obousměrného rádiového spoje se satelitem (ať už na geostacionární dráze ([GEO](/mobilnisite/slovnik/geo/)) nebo na negeostacionární satelitní dráze ([NGSO](/mobilnisite/slovnik/ngso/))) za účelem poskytnutí datového a hlasového připojení pro mobilní platformu. Terminál musí kompenzovat pohyb platformy, včetně změn polohy, orientace a rychlosti, aby udržel stabilní spojení se satelitem.

Architektonicky systém ESOMP integruje mobilní terminál, satelitní kosmický segment a pozemní bránovou pozemní stanici. Terminál ESOMP komunikuje v rádiovém kmitočtovém pásmu (jako je Ka-pásmo nebo Ku-pásmo) se satelitem, který slouží jako přenosový článek. Satelit následně komunikuje s pevnou bránovou pozemní stanicí připojenou k pozemní síti jádra (např. 5GC nebo EPC). Z pohledu sítě jádra se ESOMP jeví jako specializované uživatelské zařízení (UE) nebo skupina UE, přičemž satelitní spoj tvoří část rádiové přístupové sítě (RAN). Mezi klíčové technické komponenty patří stabilizovaný anténní systém (často mechanicky nebo elektronicky natáčený pro sledování satelitu), blokové převodníky nahoru a dolů, modemy a software pro správu mobility.

Jak to funguje, zahrnuje několik vrstevnatých procedur. Nejprve ESOMP provede zachycení satelitu: pomocí údajů o poloze (např. z [GNSS](/mobilnisite/slovnik/gnss/)) a známých efemerid satelitu namíří svou anténu a naváže počáteční spojení. Po připojení prochází procedurami připojení k síti a registrace podobnými jako u pozemního UE, ale přizpůsobenými pro delší latenci a odlišné charakteristiky spoje. ESOMP spravuje rádiový spoj, provádí přechody mezi satelitními paprsky nebo dokonce mezi různými satelity, jak se platforma pohybuje a mění se pokrytí satelitu. Specifikace 3GPP definují protokoly a rozhraní (jako jsou rozhraní N1 a [N2](/mobilnisite/slovnik/n2/) přes satelitní spoj), které umožňují ESOMP připojit se k 5G jádru, čímž umožňují standardní 3GPP služby, jako je IP připojení, QoS toky a správu relací.

Jeho role v síti spočívá v bezproblémovém rozšíření pokrytí služeb 3GPP do oblastí nedostupných pro pozemní vysílače – nad oceány, vzdálenými pevninskými územími a leteckými trasami. Umožňuje připojení za letu, námořní širokopásmové připojení a připojení pro vysokorychlostní železnice. ESOMP musí splňovat regulační omezení, jako je zabránění rušení jiným systémům a řízení vysílacího výkonu. Specifikace 3GPP (TS 38.101 pro rádiové požadavky a TS 38.108 pro technický výkon) definují minimální požadavky na ESOMP, aby byla zajištěna interoperabilita a spolehlivá služba v rámci systému 5G, přičemž satelitní spoj je považován za rádiovou přístupovou technologii definovanou 3GPP.

## K čemu slouží

Technologie ESOMP byla vytvořena, aby vyřešila kritický problém mezer v pokrytí v globálních mobilních komunikacích. Pozemní buněčné sítě poskytují vynikající pokrytí obydlených pevninských oblastí, ale nemohou pokrýt rozsáhlé regiony, jako jsou oceány, vzdušný prostor a odlehlá terestrická prostředí. To ponechává cestující a posádky na letadlech, lodích a vlacích bez spolehlivého širokopásmového přístupu. ESOMP to řeší využitím satelitních sítí, které mají téměř globální pokrytí, k poskytnutí bezproblémové služby standardizované podle 3GPP pro tyto mobilní platformy.

Historická motivace vychází z rostoucí poptávky po neustálém připojení. Zpočátku satelitní komunikace pro mobilitu využívala proprietární systémy (např. Inmarsat, Iridium) s rozhraními mimo 3GPP, což vedlo k roztříštěným uživatelským zkušenostem a složité integraci zařízení. Letecký a námořní průmysl hledal standardizovaná řešení s vysokou propustností pro internet pro cestující a provozní komunikaci. Zařazení satelitního přístupu do 5G v rámci 3GPP, vyvrcholené podrobnou prací na ESOMP ve vydání 18, bylo hnací silou vize jednotné síťové struktury, kde by se zařízení mohlo transparentně připojit prostřednictvím pozemního nebo satelitního přístupu.

ESOMP dále řeší technické výzvy specifické pro mobilitu na satelitech. Předchozí satelitní terminály pro mobilní platformy byly velké, drahé a neefektivní. Specifikace ESOMP mají za cíl standardizovat výkonnostní požadavky (jako poměr G/T a stabilita [EIRP](/mobilnisite/slovnik/eirp/)), aby podpořily konkurenceschopný ekosystém interoperabilních terminálů. Rovněž řeší regulační potřeby, jako je zajištění, že mobilní terminál při pohybu přes různé jurisdikce nezpůsobuje škodlivé rušení. Integrací ESOMP do architektury 3GPP umožňuje síťovým operátorům nabízet globální roamingové balíčky, poskytuje konzistentní servisní vrstvu pro aplikace a podporuje bezpečnostní a provozní komunikaci pro dopravní odvětví, čímž naplňuje příslib 5G o všudypřítomném připojení.

## Klíčové vlastnosti

- Standardizovaný 3GPP satelitní terminál pro letadla, lodě a vlaky
- Podpora komunikace s GEO i NGSO satelity
- Integrované stabilizované anténní systémy pro kompenzaci mobility
- Bezproblémová integrace se sítí 5G Core prostřednictvím rozhraní definovaných 3GPP (N1, N2)
- Podpora správy mobility včetně přechodu mezi paprsky a satelity
- Soulad s regulačními požadavky na emise a rušení

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements

---

📖 **Anglický originál a plná specifikace:** [ESOMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/esomp/)

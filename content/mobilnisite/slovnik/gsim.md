---
slug: "gsim"
url: "/mobilnisite/slovnik/gsim/"
type: "slovnik"
title: "GSIM – GSM Service Identity Module"
date: 2025-01-01
abbr: "GSIM"
fullName: "GSM Service Identity Module"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gsim/"
summary: "GSM Service Identity Module (GSIM) je konceptuální modul nebo identifikátor používaný v raných specifikacích 3GPP, zejména pro GPRS, k reprezentaci předplatného a profilu služeb pro paketové datové sl"
---

GSIM je konceptuální modul v raných specifikacích 3GPP, který představuje předplatné a profil služeb pro paketové datové služby, oddělující tuto identitu od fyzické SIM karty.

## Popis

GSM Service Identity Module (GSIM) je termín z raných vydání 3GPP, definovaný zejména ve specifikacích jako TS 21.905 (slovník) a TS 23.060 (popis služby [GPRS](/mobilnisite/slovnik/gprs/)). Představuje logický koncept, nikoli fyzický objekt. V kontextu služby General Packet Radio Service (GPRS) a rané paketově orientované architektury GSIM zapouzdřoval předplatitelská data a profil služeb potřebné pro přístup uživatele k paketovým datovým službám. Konceptuálně jej lze chápat jako protějšek pro paketová dat k předplatitelským datům používaným pro služby s přepojováním okruhů, ačkoli byl vnitřně propojen s fyzickou SIM/UICC.

Architektonicky by informace spojené s GSIM sídlily v síti, konkrétně v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a později v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Tato data zahrnují profily Packet Data Protocol (PDP) kontextů, které definují parametry jako povolené názvy přístupových bodů ([APN](/mobilnisite/slovnik/apn/)) uživatele, profily kvality služeb (QoS) a charakteristiky účtování. Když se mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) připojí k síti GPRS, Serving GPRS Support Node (SGSN) načte tato předplatitelská data související s GSIM z HLR/HSS v rámci procedur aktualizace polohy a autentizace. Koncept GSIM pomohl strukturovat porozumění, že identita uživatele pro služby zahrnuje více aspektů: fyzickou SIM kartu (poskytující [IMSI](/mobilnisite/slovnik/imsi/) a autentizační klíče), profil služeb s přepojováním okruhů a profil služeb s přepojováním paketů (GSIM).

V praxi je termín GSIM převážně historický a konceptuální. Funkcionalita, kterou popisoval – správa profilů předplatného pro paketová data – byla plně integrována do databáze předplatitelů (HLR/HSS) a nejedná se o samostatně nasaditelný modul. Autentizace pro GPRS stále zásadně závisela na stejném tajném klíči (Ki) uloženém na fyzické SIM a v Authentication Center (AuC). Koncept GSIM byl důležitým krokem v abstrakci služebních schopností od fyzického hardwaru a připravil cestu pro pružnější poskytování služeb. V moderní terminologii 3GPP je toto vše zahrnuto v rámci jednotné správy předplatitelských dat pro všechny typy přístupu (s přepojováním okruhů, paketů, IMS) v HSS a User Data Repository (UDR).

## K čemu slouží

Koncept GSIM vznikl během vývoje a standardizace [GPRS](/mobilnisite/slovnik/gprs/) ve 3GPP Release 4 a 5, v době, kdy se mobilní sítě vyvíjely z čistě hlasově orientovaných na podporující paketová data. Jeho účelem bylo konceptuálně modelovat a standardizovat informace o předplatném specifické pro tuto novou doménu s přepojováním paketů. Před GPRS byla předplatitelská data v [HLR](/mobilnisite/slovnik/hlr/) primárně orientována na hlasové služby s přepojováním okruhů. Zavedení trvalého, paketového přístupu k internetu vyžadovalo novou sadu parametrů profilu (jako APN a nastavení QoS).

GSIM řešil potřebu logicky oddělit a definovat tuto novou třídu předplatitelských dat. Pomohl objasnit architekturu tím, že rozlišil mezi identifikačním/autentizačním modulem (fyzická SIM) a přidruženým profilem služeb pro paketová data. Toto konceptuální oddělení bylo užitečné pro návrh specifikací, síťové modelování a pochopení, jak budou nové paketové datové služby poskytovány a spravovány nezávisle na tradičních telefonních službách. Zatímco samotný termín nepřetrval jako hmatatelná komponenta, základní princip – mít vyhrazený, spravovaný datový profil pro paketové služby vázaný na identitu předplatitele – se stal základní a integrovanou součástí všech následných architektur mobilních sítí, od 3G/UMTS přes 4G/LTE až po 5G.

## Klíčové vlastnosti

- Konceptuální reprezentace profilu předplatného pro paketové datové služby
- Obsahuje data předplatného specifická pro GPRS, jako jsou PDP kontexty a APN
- Logicky asociován s identitou předplatitele (IMSI)
- Data uložena v síťové databázi HLR/HSS
- Používána SGSN k autorizaci a konfiguraci paketových datových relací uživatele
- Historicky odlišovala profil paketových služeb od profilu služeb s přepojováním okruhů

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [GSIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/gsim/)

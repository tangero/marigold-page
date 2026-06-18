---
slug: "udhi"
url: "/mobilnisite/slovnik/udhi/"
type: "slovnik"
title: "UDHI – User Data Header Indicator"
date: 2002-01-01
abbr: "UDHI"
fullName: "User Data Header Indicator"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/udhi/"
summary: "Jednobitové pole v SMS TP-UDH, které signalizuje přítomnost hlavičky uživatelských dat (User Data Header). Je nezbytné pro umožnění pokročilých funkcí SMS, jako je spojování zpráv, adresování portů a"
---

UDHI je jednobitové pole v hlavičce SMS, které signalizuje přítomnost hlavičky uživatelských dat (User Data Header) a umožňuje pokročilé funkce, jako jsou spojené zprávy nebo adresování portů.

## Popis

Indikátor hlavičky uživatelských dat (User Data Header Indicator – UDHI) je základní součástí protokolového zásobníku služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)), konkrétně v poli přenosového protokolu pro uživatelská data (TP-UD), jak je definováno v 3GPP TS 23.040. Jedná se o jeden bit (bit 6) umístěný v oktetu schématu kódování dat [TP](/mobilnisite/slovnik/tp/) (TP-DCS) zprávy SMS-DELIVER nebo SMS-SUBMIT. Pokud je nastaven na hodnotu '1', explicitně informuje přijímající entitu – typicky mobilní stanici nebo služební centrum SMS ([SC](/mobilnisite/slovnik/sc/)) – že začátek pole TP-User-Data neobsahuje vlastní text zprávy, ale obsahuje hlavičku uživatelských dat ([UDH](/mobilnisite/slovnik/udh/)). Samotná UDH je struktura proměnné délky, která předchází uživatelskému textu a obsahuje informační prvky (IEs), které definují, jak má být zpráva zpracována nad rámec prostého zobrazení.

Při přijetí zprávy s nastaveným UDHI na 1 analyzuje protokolová vrstva přijímače pole TP-User-Data. První bajt za UDHI je interpretován jako délka hlavičky uživatelských dat ([UDHL](/mobilnisite/slovnik/udhl/)), která určuje celkovou délku v oktetech následující celé UDH. Přijímač poté přečte UDHL oktetů jako hlavičku, která obsahuje jeden nebo více informačních prvků (IEs). Každý [IE](/mobilnisite/slovnik/ie/) má specifický formát: jednooktetový identifikátor informačního prvku ([IEI](/mobilnisite/slovnik/iei/)), který definuje účel hlavičky (např. spojování, adresování portů), jednooktetovou délku dat informačního prvku (IEDL) a proměnně dlouhá data informačního prvku ([IED](/mobilnisite/slovnik/ied/)). Teprve po zpracování a odstranění této hlavičky přijímač získá přístup ke skutečnému uživatelskému textu pro zobrazení nebo použití aplikací.

Z architektonického hlediska UDHI funguje na aplikační vrstvě v rámci protokolu SMS, rozhraní mezi aplikacemi vyšší vrstvy (jako jsou klienti pro zasílání zpráv) a transportní vrstvou nižší úrovně. Jeho role je čistě indikativní; nepřenáší sama o sobě data, ale spouští zpracování hlavičky. Tento mechanismus je klíčový pro zachování zpětné kompatibility. Zařízení nebo síťové prvky, které nepodporují UDHI/UDH (nebo je ignorují), mohou zobrazovat oktety hlavičky jako zkomolený text, ale základní doručení zprávy není znemožněno. UDHI umožňuje čisté oddělení mezi řídicími informacemi (v UDH) a uživatelskou datovou částí, což umožňuje rozšiřitelné funkce SMS bez nutnosti měnit základní strukturu vrstvy TP pro každou novou schopnost.

## K čemu slouží

UDHI bylo zavedeno, aby vyřešilo inherentní omezení původního návrhu SMS, který byl koncipován pro jednoduché, krátké textové zprávy bez ustanovení pro pokročilé funkčnosti. Zpočátku byly SMS zprávy omezeny na 160 znaků při použití výchozí 7bitové GSM abecedy a neměly standardizovaný způsob, jak indikovat, že zpráva obsahuje dodatečné řídicí informace pro funkce jako spojování dlouhých zpráv, směrování zpráv ke konkrétním aplikacím na terminálu (např. stahování vyzvánění, WAP push) nebo definování tříd zpráv. Bez indikátoru hlavičky vyžadovala implementace takových funkcí proprietární, neinteroperabilní řešení nebo signalizaci 'v pásmu', která narušovala uživatelsky viditelný text.

Vytvoření UDHI spolu s úplnou specifikací UDH poskytlo standardizovaný, rozšiřitelný rámec v rámci existující obálky SMS TP. Vyřešilo problém tím, že vyhradilo jeden bit, aby sloužil jako příznak – minimální režie, která odemkla významnou funkcionalitu. To umožnilo síťovým operátorům a výrobcům terminálů konzistentně nasazovat služby s přidanou hodnotou na různých zařízeních a sítích. Motivace byla z velké části komerční a technická: vyvinout SMS z jednoduché služby pro zasílání textů mezi osobami na platformu pro doručování obsahu a služeb od aplikace k osobě, čímž se zvýšil průměrný výnos na uživatele (ARPU), aniž by bylo nutné zásadně přepracovat již široce nasazenou infrastrukturu GSM/UMTS.

Historicky jeho zavedení v 3GPP Release 5 (ačkoli vychází z dřívějších specifikací GSM Phase 2+) formalizovalo tyto schopnosti v rámci 3GPP, což zajistilo interoperabilitu pro sítě 3G UMTS a novější. Vyřešilo kritický problém zpětné a dopředné kompatibility; staré terminály mohly stále přijímat zprávy (i když zobrazovaly bajty hlavičky) a nové terminály mohly správně interpretovat pokročilé funkce. Tento konstrukční princip použití lehkého indikátoru k umožnění bohaté struktury hlavičky učinil z UDHI na desetiletí základní kámen rozšířených služeb SMS.

## Klíčové vlastnosti

- Jednobitový příznak v TP-DCS indikující přítomnost UDH
- Umožňuje zpracování hlavičky uživatelských dat (UDH) pro pokročilé SMS
- Zachovává zpětnou kompatibilitu se staršími SMS zařízeními
- Spouští analýzu UDHL a následných informačních prvků
- Nezbytné pro spojování SMS a adresování aplikačních portů
- Definováno v 3GPP TS 23.040/23.048 pro standardizovanou interoperabilitu

## Související pojmy

- [UDHL – User Data Header Length](/mobilnisite/slovnik/udhl/)
- [UDH – User Data Header](/mobilnisite/slovnik/udh/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [UDHI na 3GPP Explorer](https://3gpp-explorer.com/glossary/udhi/)

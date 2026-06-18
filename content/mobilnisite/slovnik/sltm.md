---
slug: "sltm"
url: "/mobilnisite/slovnik/sltm/"
type: "slovnik"
title: "SLTM – Signalling Link Test Message"
date: 2025-01-01
abbr: "SLTM"
fullName: "Signalling Link Test Message"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sltm/"
summary: "Protokolová zpráva používaná v signalizačních sítích založených na SS7 k ověření provozního stavu signalizačního spoje. Je klíčovým údržbovým a diagnostickým nástrojem, který zajišťuje spolehlivou sig"
---

SLTM je protokolová zpráva používaná v signalizačních sítích SS7 k ověření provozního stavu signalizačního spoje; slouží jako údržbový nástroj pro zajištění konektivity mezi uzly, jako jsou MSC a HLR.

## Popis

Zpráva pro test signalizačního spoje (Signalling Link Test Message, SLTM) je základní součástí správy signalizační sítě na úrovni [MTP](/mobilnisite/slovnik/mtp/) (Message Transfer Part) 3 v rámci protokolové sady [SS7](/mobilnisite/slovnik/ss7/)/C7, jak ji přijala a rozšířila organizace 3GPP pro signalizaci v jádru sítě. Funguje přes signalizační datový spoj (např. 64kbps časový slot) mezi dvěma signalizačními body, jako je ústředna mobilního spojení (Mobile Switching Center, [MSC](/mobilnisite/slovnik/msc/)) a registr domovských účastníků (Home Location Register, [HLR](/mobilnisite/slovnik/hlr/)). Primární funkcí SLTM je proaktivní ověření spoje. Signalizační bod periodicky generuje a vysílá SLTM k sousednímu signalizačnímu bodu po spoji, který je ve stavu 'zarovnání' ('aligned') nebo 'ověřování' ('proving') během počátečního nastavování, nebo po neaktivním spoji ve stavu 'zastaveno' ('stopped') pro periodické testování. Zpráva obsahuje testovací vzor, často pseudonáhodnou bitovou sekvenci, a časové razítko. Po přijetí musí sousední bod odpovědět potvrzovací zprávou pro test signalizačního spoje (Signalling Link Test Acknowledgment, SLTA), která opakuje přijatý testovací vzor. Tato výměna potvrzuje obousměrnou integritu signalizačního spoje na úrovni MTP 2 (vrstvě datového spoje), ověřuje, že rámce mohou být před doručením živého provozu nebo při podezření na poruchu správně doručeny, seřazeny a potvrzeny.

Architektura pro zpracování SLTM je vestavěna do funkcí správy signalizačních spojů každého signalizačního bodu. Když je spoj vyřazen z provozu nebo je v pohotovostní skupině, vrstva správy sítě může zahájit testovací proceduru. Výměna SLTM/SLTA testuje celou lokální i vzdálenou zpracovatelskou cestu MTP úrovně 2, včetně hardwaru koncového zařízení spoje a přenosového zařízení. Nedoručení platné SLTA v časovém limitu nebo přijetí poškozeného vzoru signalizuje poruchu. To spouští lokální diagnostiku a může zabránit zařazení spoje do provozu nebo způsobit jeho vyřazení, čímž se zajišťuje, že pouze spolehlivé spoje jsou používány pro kritickou signalizaci, jako je建立ování hovorů a správa mobility.

Její role je zásadní pro spolehlivost sítě. V jádru sítě 3GPP s přepojováním okruhů přenášejí signalizační spoje zásadní zprávy pro správu mobility (např. aktualizace polohy), řízení hovorů a doplňkové služby. Porouchaný spoj zařazený do provozu bez odhalení by mohl způsobit ztrátu zpráv, vedoucí k přerušeným hovorům nebo neúspěšným registracím. Vyžadováním úspěšného handshake SLTM/SLTA síť zajišťuje základní úroveň kvality pro každou signalizační cestu. To je součástí širších principů správy sítě SS7 týkajících se dostupnosti a spolehlivosti, které 3GPP jádro sítě přímo přebírá ze svého dědictví GSM/UMTS. Procedura je automatická a za normálních podmínek nevyžaduje manuální zásah, čímž vytváří kontinuální samokontrolní mechanismus pro signalizační infrastrukturu.

## K čemu slouží

SLTM existuje, aby řešila kritický problém neodhalených poruch signalizačních spojů v telekomunikačních sítích. Před zavedením automatického testování spojů mohly být poruchy odhaleny až poté, co byl ovlivněn živý provoz, což vedlo ke zhoršení služeb. Architektura [SS7](/mobilnisite/slovnik/ss7/), navržená pro veřejné telefonní sítě s vysokou spolehlivostí, vyžadovala mechanismus pro ověření stavu signalizační cesty před tím, než je na ni nasměrován uživatelský provoz. SLTM poskytuje tuto proaktivní ověřovací schopnost.

Historicky, jak se sítě vyvíjely od signalizace v pásmu (kde řídicí a hlasový kanál sdílely stejný kanál) k signalizaci s společným kanálem (Common Channel Signalling, [CCS](/mobilnisite/slovnik/ccs/)) mimo pásmo se SS7, stala se signalizační síť samostatnou entitou s vysokou dostupností. Porucha jediného signalizačního spoje mohla ovlivnit tisíce hovorů. Procedura SLTM byla zavedena jako součást robustní sady nástrojů pro správu SS7, aby zajistila, že každý spoj zařazený do provozu splňuje minimální provozní kritéria. Řeší omezení čistě pasivního monitorování nebo reaktivních systémů založených na alarmech tím, že aktivně prověřuje spoj, testuje jak integritu přenosu, tak i zpracovatelskou logiku na obou koncích.

V kontextu 3GPP zůstává tento účel nezměněn. Od GSM Release 99 výše se jádro sítě spoléhalo na SS7 pro kritická rozhraní, jako jsou rozhraní B, C, D a E. SLTM zajišťuje, že základní signalizační přenos pro legacy služby s přepojováním okruhů je spolehlivý. I když se sítě vyvíjejí směrem k plně IP s protokoly Diameter a [HTTP](/mobilnisite/slovnik/http/)/2, princip aktivní kontroly stavu spojení přetrvává v nových protokolech, což demonstruje trvalou potřebu, kterou paradigma SLTM řešilo.

## Klíčové vlastnosti

- Proaktivní ověření spoje před přenosem živého signalizačního provozu
- Obousměrný test potvrzující integritu na úrovni MTP 2
- Používá definovaný testovací vzor a vyžaduje specifické potvrzení (SLTA)
- Integrální součást procedur správy a zarovnávání signalizačních spojů SS7
- Při selhání testu spouští automatickou izolaci poruchy a deaktivaci spoje
- Funguje na aktivních (pro periodické kontroly) i neaktivních/pohotovostních spojích

## Související pojmy

- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [SLTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sltm/)

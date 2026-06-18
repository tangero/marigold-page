---
slug: "t-ue"
url: "/mobilnisite/slovnik/t-ue/"
type: "slovnik"
title: "T-UE – Terminating User Equipment"
date: 2025-01-01
abbr: "T-UE"
fullName: "Terminating User Equipment"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-ue/"
summary: "T-UE označuje uživatelské zařízení (UE), které je příjemcem nebo koncovým bodem komunikační relace, například volaná strana při hlasovém hovoru nebo cíl pro data. Jde o klíčový koncept v řízení relací"
---

T-UE je uživatelské zařízení (UE), které je koncovým bodem nebo příjemcem komunikační relace, například volaná strana při hlasovém hovoru.

## Popis

Terminating User Equipment ([T-UE](/mobilnisite/slovnik/t1/)) je logický identifikátor používaný ve specifikacích 3GPP pro označení uživatelského zařízení, které je cílem nebo koncovým bodem komunikační relace. V kontextu řízení hovorů, navazování relací a procedur mobility musí síť rozlišovat mezi iniciujícím UE (volající nebo odesílatel) a koncovým UE (volaný nebo příjemce). T-UE je identifikováno přihlašovacími údaji účastníka, jako je [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/), a jeho aktuální polohou nebo obsluhujícím síťovým uzlem. Tento koncept je nedílnou součástí procedur jako je sestavení hovoru, předávání spojení a poskytování služeb, kde síť musí směrovat signalizační a uživatelskou provozní plochu na správné cílové zařízení.

Z architektonického hlediska identifikaci T-UE spravují entity jádra sítě, konkrétně Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro okruhově spínané služby nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) pro paketově spínané služby v pozdějších vydáních. Při sestavování relace signalizační zprávy (např. v [ISUP](/mobilnisite/slovnik/isup/) nebo [SIP](/mobilnisite/slovnik/sip/)) nesou identifikátory pro iniciující i koncovou stranu. Síť tyto informace využívá k provedení směrování, vyhledávání (paging) a přidělování prostředků specificky pro T-UE. Kontext T-UE, včetně jeho schopností, předplacených služeb a aktuálních rádiových podmínek, ovlivňuje způsob, jakým síť zpracovává příchozí požadavek na relaci.

Jak to funguje, zahrnuje několik síťových funkcí: když je relace iniciována směrem k účastníkovi, síť dotazuje databáze jako Home Location Register (HLR) nebo Home Subscriber Server (HSS), aby zjistila stav T-UE a obsluhující síť. Následně jsou v poslední známé sledované oblasti nebo směrovací oblasti provedeny procedury vyhledávání (paging) k lokalizaci T-UE. Po lokalizaci síť směrem k T-UE zřídí přenosový kanál (bearer) nebo okruh, čímž spojení dokončí. Koncept T-UE zajišťuje, že řízení relací a procedury mobility jsou správně aplikovány z perspektivy přijímací strany, což je klíčové pro spolehlivou a efektivní telekomunikaci.

## K čemu slouží

Koncept T-UE existuje proto, aby poskytoval jasný a standardizovaný referenční bod pro cílovou stranu jakékoli komunikační relace v systémech 3GPP. V telekomunikacích má každé spojení dva koncové body: iniciátora a terminátora. Explicitní definice T-UE umožňuje protokolovým specifikacím, jako jsou specifikace pro řízení hovorů (TS 23.172) a správu mobility, jednoznačně popsat procedury, toky zpráv a stavové automaty z pohledu koncové strany. Tato jasnost je zásadní pro interoperabilitu a správné chování sítě.

Historicky, jak se sítě vyvíjely od jednoduchých hlasových hovorů ke komplexním multimediálním relacím, potřeba samostatně spravovat koncovou stranu se stala výraznější. Například funkce jako přesměrování hovoru, restrikce přístupu pro ukončení a spouštění služeb závisí na znalosti toho, které UE je cílem. Označení T-UE pomáhá oddělit logiku a politiky, které platí pouze pro přijímajícího účastníka, jako je kontrola obsazenosti, aplikace tarifování volané strany nebo provádění služeb založených na poloze pro volaného. Řeší tak omezení pouhého obecného konceptu „UE“, který nerozlišuje roli v relaci, a umožňuje tak sofistikovanější obsluhu služeb a optimalizaci sítě.

## Klíčové vlastnosti

- Identifikuje cílové UE v komunikační relaci
- Používá se v procedurách řízení hovorů a sestavování relací
- Umožňuje cílené vyhledávání (paging) a správu polohy
- Podporuje spouštění služeb pro volanou stranu
- Usnadňuje směrování signalizace a uživatelské provozní plochy na správné zařízení
- Je nedílnou součástí procedur mobility, jako je předávání spojení (handover) pro koncovou stranu

## Související pojmy

- [O-UE – Originating User Equipment](/mobilnisite/slovnik/o-ue/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)

---

📖 **Anglický originál a plná specifikace:** [T-UE na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-ue/)

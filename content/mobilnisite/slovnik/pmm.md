---
slug: "pmm"
url: "/mobilnisite/slovnik/pmm/"
type: "slovnik"
title: "PMM – Packet Mobility Management"
date: 2025-01-01
abbr: "PMM"
fullName: "Packet Mobility Management"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pmm/"
summary: "Packet Mobility Management (PMM) je model stavů v jádru sítě pro paketově orientované služby GPRS a UMTS. Sleduje stav mobility a připojení uživatelského zařízení (UE) mezi Serving GPRS Support Node ("
---

PMM je model stavů v jádru sítě pro GPRS a UMTS, který sleduje mobilitu a připojení uživatelského zařízení mezi SGSN a UE pro přidělování prostředků a mobilní procedury.

## Popis

Packet Mobility Management (PMM) je základní model stavů definovaný v architektuře paketově orientovaného jádra sítě 3GPP pro [GPRS](/mobilnisite/slovnik/gprs/) a UMTS, konkrétně mezi uživatelským zařízením (UE) a Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)). Definuje stavy připojení a mobility UE pro paketově orientované služby, což je odlišné od správy mobility v okruhově orientované doméně ([CS](/mobilnisite/slovnik/cs/)), kterou zajišťuje Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)). Model PMM je klíčový pro to, aby síť znala polohu UE a jeho připravenost k odesílání či příjmu paketových dat, což přímo ovlivňuje přidělování prostředků, efektivitu vyhledávání a správu relací.

Stav PMM je udržován jak v UE, tak v SGSN a musí být synchronizován. Hlavní stavy PMM jsou PMM-IDLE, PMM-CONNECTED a PMM-DETACHED. Ve stavu PMM-IDLE má UE navázaný Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) kontext (IP adresu), ale nemá aktivní rádiové spojení; SGSN zná směrovací oblast ([RA](/mobilnisite/slovnik/ra/)) UE, nikoli však přesnou buňku. Síť musí UE v jeho poslední známé RA vyhledat (paging), aby doručila downlink data, což spustí přechod do PMM-CONNECTED. Ve stavu PMM-CONNECTED má UE aktivní rádiové spojení (např. spojení Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) v [UTRAN](/mobilnisite/slovnik/utran/)) a SGSN zná aktuální buňku nebo skupinu buněk UE. Tento stav umožňuje okamžitý přenos dat. PMM-DETACHED značí, že UE není registrováno pro paketově orientované služby; neexistuje PDP kontext a SGSN nemá platné informace o poloze UE.

Přechody mezi těmito stavy jsou spouštěny konkrétními procedurami. UE přechází z PMM-IDLE do PMM-CONNECTED prostřednictvím procedury Service Request iniciované UE pro uplink data nebo jako odpověď na síťové vyhledání (paging) pro downlink data. Může k tomu také dojít v důsledku procedury aktualizace směrovací oblasti (RAU) při pohybu UE. Přechod z PMM-CONNECTED do PMM-IDLE typicky nastane po vypršení časovače nečinnosti, kdy síť uvolní rádiové spojení, ale zachová PDP kontext. Procedura GPRS Attach přesune UE ze stavu PMM-DETACHED do PMM-IDLE (nebo přímo do PMM-CONNECTED, pokud okamžitě začne přenos dat), zatímco procedura Detach jej přesune do PMM-DETACHED. Stav PMM je úzce provázán se stavem PDP kontextu a se stavem správy mobility (MM) v okruhově orientované doméně, ačkoli jsou řízeny nezávisle.

Role PMM je ústřední pro fungování paketových datových sítí 2.5G a 3G. Umožňuje síti šetřit rádiové a síťové prostředky tím, že UE mohou zůstat v nízkopříkonovém stavu PMM-IDLE, když aktivně nekomunikují, a přitom zůstávají dosažitelná pro příchozí data. Poskytuje základ pro mobilitu, umožňuje SGSN sledovat polohu UE na úrovni směrovací oblasti a spravovat předávání mezi různými SGSN. Synchronizace stavu PMM mezi UE a SGSN zajišťuje konzistentní chování pro správu relací, účtování a zákonné odposlechy. Zatímco se tento koncept vyvinul v model stavů EPS Mobility Management (EMM) v LTE/EPC a model stavů 5G Mobility Management (5GMM) v 5G systému (5GS), PMM zůstává kritickým protokolem pro správu stavů v legacy sítích UMTS a GPRS.

## K čemu slouží

Packet Mobility Management byl vytvořen, aby do původně na okruhovou doménu orientované sítě GSM 2G zavedl efektivní, nespojované paketové datové služby. Před GPRS bylo GSM navrženo primárně pro hlasové hovory, které vyžadovaly vyhrazené, nepřetržité okruhově orientované spojení. Tento model byl neefektivní pro přerušovaný, dávkový datový provoz typický pro rané internetové aplikace jako e-mail a prohlížení webu, protože by nepřetržitě vázal cenné rádiové a síťové prostředky. Účelem PMM bylo definovat model stavů, který by mohl podporovat "stále zapojené" IP připojení bez nutnosti trvalého rádiového spojení, čímž by optimalizoval využití prostředků a umožnil nové datové služby.

Základní problém, který PMM řešil, bylo, jak sledovat polohu mobilního zařízení a jeho připravenost k přenosu paketových dat, a zároveň mu umožnit vypnout rádiový vysílač/přijímač pro úsporu baterie v době nečinnosti. Bez takového modelu by síť musela buď neustále udržovat plné rádiové spojení (plýtvání), nebo o zařízení zcela ztratit přehled (čímž by se stalo nedosažitelným). PMM zavedl mezistav PMM-IDLE, kdy je zařízení registrováno, má IP adresu (PDP kontext), ale nemá aktivní rádiový spoj. Síť zná polohu zařízení na úrovni směrovací oblasti (skupina buněk), což umožňuje efektivní vyhledání (paging) pro opětovné navázání spojení, když je potřeba. To byl revoluční posun od okruhově orientovaného modelu a otevřelo to cestu mobilnímu internetu.

Dále PMM poskytlo strukturovaný rámec pro mobilitu v paketově orientované doméně. Definovalo jasné procedury pro připojení (attach), odpojení (detach), aktualizaci směrovací oblasti (RAU) a žádosti o službu (service request), které byly nezbytné pro bezproblémový uživatelský zážitek při pohybu. Také umožnilo jádru sítě spravovat prostředky jako kontexty SGSN a GTP tunely na základě stavu UE. Vytvoření PMM bylo základním krokem ve vývoji mobilních sítí z čistě telefonních systémů na platformy pro obecnou datovou komunikaci, což přímo umožnilo následné mobilní datové služby.

## Klíčové vlastnosti

- Definuje tři hlavní stavy: PMM-DETACHED, PMM-IDLE a PMM-CONNECTED pro paketové připojení UE
- Umožňuje efektivní využití rádiových prostředků tím, že UE mohou setrvávat v nízkopříkonovém stavu PMM-IDLE
- Podporuje komunikaci iniciovanou sítí prostřednictvím procedur vyhledání (paging) spouštěných ze stavu PMM-IDLE
- Poskytuje rámec pro procedury správy mobility, jako je GPRS Attach, Detach a aktualizace směrovací oblasti (RAU)
- Synchronizuje stav mezi uživatelským zařízením (UE) a Serving GPRS Support Node (SGSN)
- Tvoří základ pro aktivaci Packet Data Protocol (PDP) kontextu a správu relací

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [EMM – Evolved Mobility Management](/mobilnisite/slovnik/emm/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2

---

📖 **Anglický originál a plná specifikace:** [PMM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmm/)

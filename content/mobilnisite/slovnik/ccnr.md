---
slug: "ccnr"
url: "/mobilnisite/slovnik/ccnr/"
type: "slovnik"
title: "CCNR – Completion of Communication sessions on No Reply"
date: 2025-01-01
abbr: "CCNR"
fullName: "Completion of Communication sessions on No Reply"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ccnr/"
summary: "CCNR je doplňková služba, která umožňuje volající straně požádat o dokončení komunikační relace, když je volaná strana obsazená nebo neodpovídá. Umožňuje automatické navázání hovoru, když se volaná st"
---

CCNR je doplňková služba, která automaticky dokončí komunikační relaci volajícímu, když se volaná strana, která byla obsazená nebo neodpověděla, stane dostupnou.

## Popis

Completion of Communication sessions on No Reply (CCNR) je standardizovaná doplňková služba v sítích 3GPP, která poskytuje funkci automatického dokončení hovoru, když počáteční pokusy o spojení selžou z důvodu obsazenosti nebo neodpovědi volané strany. Služba funguje prostřednictvím síťového mechanismu front, kde je žádost volající strany uložena a monitorována, dokud se volaný účastník nestane dostupným pro komunikaci. Po aktivaci CCNR zachytí neúspěšné pokusy o spojení a převede je do čekacího stavu namísto okamžitého ukončení spojení.

Z architektonického hlediska je CCNR implementována v prvcích core sítě, primárně za účasti Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro správu dat účastníků a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo IP Multimedia Subsystem (IMS) uzlů pro zpracování hovorů. Služba se opírá o specifické signalizační procedury definované ve specifikacích 3GPP pro vytvoření, udržování a ukončení žádosti o dokončení. Když uživatel aktivuje CCNR pro neúspěšný hovor, síť vytvoří záznam o dokončení obsahující identity volající a volané strany, časové razítko a parametry služby. Tento záznam je uložen v příslušném síťovém prvku na základě registračního stavu volané strany a konfigurace sítě.

Služba funguje prostřednictvím monitorovacího mechanismu, který sleduje stav dostupnosti volané strany. Když volaný účastník přejde ze stavu obsazeno nebo nedostupný do stavu volný a registrovaný, síť tuto změnu stavu detekuje a zahájí proceduru dokončení. Síť poté automaticky pokusí navázat komunikační relaci a obě strany o tom informuje pomocí specifických tónů nebo indikací. Implementace zahrnuje časovače a čítače, aby se zabránilo neomezenému čekání ve frontě, s konfigurovatelnými dobami vypršení a maximálním počtem opakovaných pokusů. CCNR se integruje s dalšími doplňkovými službami, jako je přesměrování hovorů nebo zákaz hovorů, s definovanými pravidly přednosti, aby se předešlo konfliktům mezi různými službami.

Mezi klíčové technické komponenty patří procedury aktivace/deaktivace CCNR, ukládání a správa žádostí o dokončení, mechanismy monitorování dostupnosti a protokoly pro automatické navazování hovorů. Služba podporuje jak hlasové, tak multimediální relace v prostředí IMS, se specifickými úpravami pro různé typy relací. Bezpečnostní opatření zajišťují, že službu mohou aktivovat pouze autorizovaní uživatelé a že pokusy o dokončení následují příslušné autentizační procedury. Implementace CCNR se liší mezi okruhově přepínanou a paketově přepínanou doménou, přičemž implementace založené na IMS nabízejí vyšší flexibilitu a integraci s dalšími multimediálními službami.

## K čemu slouží

CCNR byla vyvinuta k řešení běžného problému neúspěšných pokusů o komunikaci v mobilních sítích, zejména když uživatelé narazí na obsazený signál nebo situaci bez odpovědi. Před CCNR museli volající opakovaně zkoušet spojení ručně, což bylo neefektivní a frustrující. Tato služba tento proces automatizuje a umožňuje uživatelům požádat o automatické dokončení, jakmile se volaná strana stane dostupnou, čímž zvyšuje míru úspěšnosti komunikace a uživatelský komfort.

Historicky podobné služby existovaly v pevných sítích (často nazývané 'call completion to busy subscriber' nebo [CCBS](/mobilnisite/slovnik/ccbs/)), ale 3GPP standardizovalo CCNR speciálně pro mobilní prostředí, kde mobilita účastníků a jejich registrační stavy přidávaly složitost. Služba řeší omezení základního zpracování hovorů, kde neúspěšné pokusy jednoduše skončily bez možnosti nápravy. Zavedením front pro dokončení spravovaných sítí CCNR snižuje počet zmeškaných spojení a zlepšuje celkové využití sítě tím, že zajišťuje, že pokusy o komunikaci nakonec uspějí, když to podmínky dovolí.

Vznik CCNR byl motivován potřebou vylepšit základní telefonní služby v mobilních sítích tak, aby odpovídaly nebo překonávaly možnosti pevných linek. Řeší problém neefektivních ručních opakovaných pokusů a zvyšuje spokojenost zákazníků tím, že zajišťuje, že důležité komunikace nejsou zmeškány z důvodu dočasné nedostupnosti. V obchodním kontextu CCNR zajišťuje dokončení kritických hovorů bez nutnosti neustálého monitorování volající stranou, což je zvláště cenné pro časově citlivou komunikaci.

## Klíčové vlastnosti

- Automatické dokončení hovoru, když volaná strana přejde ze stavu obsazeno/nedostupno do stavu dostupno
- Síťový mechanismus front s konfigurovatelnými časovými limity
- Podpora jak okruhově přepínaných, tak IMS-based multimediálních relací
- Integrace s dalšími doplňkovými službami prostřednictvím definovaných pravidel přednosti
- Aktivace/deaktivace řízená účastníkem se standardizovanými procedurami
- Monitorování dostupnosti prostřednictvím mechanismů sledování registrace a stavu

## Související pojmy

- [CCBS – Completion of Communications to Busy Subscriber](/mobilnisite/slovnik/ccbs/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.642** (Rel-19) — CCBS/CCNR/CCNL SIP Protocol Specification
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony
- **TS 32.275** (Rel-19) — MMTel Charging Specification
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study

---

📖 **Anglický originál a plná specifikace:** [CCNR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccnr/)

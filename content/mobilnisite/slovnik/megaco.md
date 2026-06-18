---
slug: "megaco"
url: "/mobilnisite/slovnik/megaco/"
type: "slovnik"
title: "MEGACO – MEdia GAteway COntrol"
date: 2025-01-01
abbr: "MEGACO"
fullName: "MEdia GAteway COntrol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/megaco/"
summary: "Protokol typu master-slave definovaný IETF a přijatý 3GPP pro řízení mediálních bran (MGW) z kontroléru mediálních bran (MGC). Odděluje inteligenci řízení hovoru od zpracování médií, což umožňuje škál"
---

MEGACO je protokol typu master-slave pro řízení mediálních bran (Media Gateway) z kontroléru mediálních bran (Media Gateway Controller), který odděluje řízení hovoru od zpracování médií za účelem umožnění propojení sítí s přepojováním okruhů a paketů.

## Popis

MEGACO, známý také jako H.248, je textový řídicí protokol aplikační vrstvy používaný pro řízení entit Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) v dekomponované architektuře brány. V rámci architektury 3GPP se používá primárně v kontextu funkčního rozdělení mezi Media Gateway (MGW) a Media Gateway Controller ([MGC](/mobilnisite/slovnik/mgc/)), často spojovaného s [MSC](/mobilnisite/slovnik/msc/) Serverem ([MSC-S](/mobilnisite/slovnik/msc-s/)) a MGW v jádru s přepojováním okruhů. Protokol funguje na modelu master-slave, kde MGC (master, např. MSC Server) vydává příkazy MGW (slave) pro manipulaci s "kontexty" a "terminacemi", které reprezentují mediální toky a spojení.

"Terminace" v MEGACO je zdroj nebo cíl jednoho či více mediálních toků, například časový slot na [TDM](/mobilnisite/slovnik/tdm/) trunku (strana s přepojováním okruhů) nebo [RTP](/mobilnisite/slovnik/rtp/) port na IP rozhraní (strana s přepojováním paketů). Terminace mají vlastnosti popsané deskriptory, které zahrnují signály (např. tóny k přehrání), události (např. detekci [DTMF](/mobilnisite/slovnik/dtmf/) číslic) a statistiky (např. odeslané pakety). "Kontext" je asociace mezi více terminacemi, kde dochází k mixování nebo přepojování médií; prázdný kontext značí nulovou asociaci. MGC používá příkazy jako Add, Modify, Subtract, Move a AuditValue k instruování MGW, aby vytvořila kontexty, přidala do nich terminace, upravila parametry toků nebo je zrušila.

Jak funguje: Při sestavování hovoru MSC Server (MGC) určí potřebu vytvoření mediální cesty přes MGW. Použije MEGACO přes IP spojení k vydání příkazů MGW, aby vytvořila nový kontext, přidala terminaci reprezentující větev s přepojováním okruhů (např. od [BSC](/mobilnisite/slovnik/bsc/)) a přidala další terminaci reprezentující větev s přepojováním paketů (např. směrem k IMS nebo jiné MGW). MGW tyto příkazy provede, vytvoří interní funkci propojení nebo transkódování mezi terminacemi a vrátí potvrzení. Protokol také umožňuje MGW notifikovat MGC o událostech detekovaných na terminacích, jako je hook-flash nebo faxové tóny. Toto jasné oddělení umožňuje MGC soustředit se na stav hovoru a signalizaci (např. ISUP, BICC), zatímco MGW se stará o fyzické/mediální zpracování, což umožňuje centralizované řízení a distribuované, škálovatelné zpracování médií.

## K čemu slouží

MEGACO byl vyvinut k řešení problému monolitických, proprietárních a nepružných telefonních ústředen. Tradiční ústředny s přepojováním okruhů (jako Class-5 ústředny nebo rané MSC) integrovaly řízení hovoru a fyzickou přepínací strukturu (prohození časových slotů) do jediné, drahé a vertikálně integrované platformy. To ztěžovalo škálování sítě, zavádění nových služeb a interoperabilitu mezi dodavateli. Účelem MEGACO je umožnit dekomponovanou architekturu založenou na otevřených standardech, která odděluje řízení hovoru (inteligenci) od přepínání/zpracování médií (strukturu).

Toto oddělení, motivované přechodem k páteřním sítím s přepojováním paketů (jako IP), umožnilo operátorům nasazovat levnější, škálovatelné mediální brány od jednoho dodavatele a sofistikované servery řízení hovoru od jiného, což podpořilo konkurenci a inovace. Přímo řešilo omezení dřívějších řídicích protokolů jako MGCP, které byly méně flexibilní. V kontextu 3GPP bylo jeho přijetí (počínaje Release 2 pro 3G UMTS) motivováno potřebou vyvinout jádro s přepojováním okruhů pro podporu řízení hovoru nezávislého na nosiči. To umožnilo operátorům převést svá jádrové sítě z tradičních ústředen založených na TDM na nákladově efektivnější a budoucím vývojům lépe odolávající infrastrukturu založenou na IP, při zachování interoperability se staršími sítěmi s přepojováním okruhů (PSTN, 2G GSM).

## Klíčové vlastnosti

- Řídicí protokol typu master-slave mezi MGC a MGW
- Manipulace s abstraktními entitami: Kontexty a Terminace
- Podpora širokého spektra typů médií a kódování
- Balíčky událostí a signálů pro flexibilní tvorbu služeb
- Textové kódování (formát ASN.1 text) pro čitelnost
- Robustní zpracování chyb a možnosti auditu

## Související pojmy

- [MGC – Media Gateway Controller](/mobilnisite/slovnik/mgc/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking

---

📖 **Anglický originál a plná specifikace:** [MEGACO na 3GPP Explorer](https://3gpp-explorer.com/glossary/megaco/)

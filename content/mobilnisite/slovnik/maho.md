---
slug: "maho"
url: "/mobilnisite/slovnik/maho/"
type: "slovnik"
title: "MAHO – Mobile Assisted Handover"
date: 2025-01-01
abbr: "MAHO"
fullName: "Mobile Assisted Handover"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/maho/"
summary: "Mechanismus předávání hovoru, při kterém mobilní stanice (MS) napomáhá síti prováděním rádiových měření okolních buněk. MS tato měření hlásí síti, která následně učiní konečné rozhodnutí o předání. Te"
---

MAHO je mechanismus předávání hovoru, při kterém mobilní stanice napomáhá síti měřením okolních buněk a jejich hlášením, což síti umožňuje učinit konečné rozhodnutí o předání hovoru za účelem udržení kvality spojení.

## Popis

Mobile Assisted Handover (MAHO) je základní procedura správy mobility v sítích 2G GSM a 3G UMTS. V této architektuře je mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelské zařízení (UE) aktivním účastníkem fáze přípravy předání hovoru. Zatímco je připojena k obsluhující buňce, MS kontinuálně měří sílu signálu (RXLEV) a kvalitu (RXQUAL) svého aktuálního kanálu řídicího vysílání ([BCCH](/mobilnisite/slovnik/bcch/)) a během nečinných rámců se ladí na kanály řídicího vysílání okolních buněk podle seznamu přidělení BCCH ([BA](/mobilnisite/slovnik/ba/)), který poskytuje síť. Tato měření jsou periodicky hlášena podsystému základnové stanice ([BSS](/mobilnisite/slovnik/bss/)) prostřednictvím hlášení o měření na pomalém přidruženém řídicím kanálu (SACCH).

Síťová strana, konkrétně řadič základnové stanice ([BSC](/mobilnisite/slovnik/bsc/)) v GSM nebo řadič rádiové sítě (RNC) v UMTS, agreguje tato hlášení o měření od všech připojených mobilů. BSC/RNC spouští složité algoritmy předávání hovoru, které vyhodnocují nahlášená data vůči sadě konfigurovatelných prahových hodnot a parametrů hystereze. Algoritmus zvažuje faktory jako přijímaná úroveň signálu, kvalita signálu, vzdálenost (pomocí časového předstihu), rušení a zatížení sítě. Základním principem MAHO je oddělení rolí: mobil napomáhá shromažďováním rádiových dat, ale síť si ponechává plnou kontrolu nad konečným rozhodnutím, čímž zajišťuje centralizovanou správu zdrojů a koordinaci rušení.

Rozhodnutí o předání hovoru učiněné BSC/RNC může spustit různé typy předání, jako je předání uvnitř buňky (z důvodu provozu), uvnitř BSC, mezi BSC nebo dokonce mezi [MSC](/mobilnisite/slovnik/msc/). Jakmile je rozhodnutí učiněno, síť pošle mobilní stanici příkaz k předání hovoru na rychlém přidruženém řídicím kanálu ([FACCH](/mobilnisite/slovnik/facch/)), nařizující jí naladit se na nový kanál pro přenos hovoru (TCH) v cílové buňce. MS poté přistoupí k novému kanálu a síť dokončí přepojení hlasové cesty. Celý tento proces, umožněný MAHO, probíhá nepozorovatelně, aby podporoval mobilitu při rychlostech vozidel, a je klíčový pro minimalizaci přerušení hovoru a udržení kontinuity služby.

## K čemu slouží

MAHO byl vytvořen, aby vyřešil základní výzvu udržení kontinuálního spojení s přepojováním okruhů (jako je hlasový hovor) pro uživatele pohybujícího se v celulární síti složené z mnoha malých rádiových buněk. Předchozí celulární systémy často používaly pouze síťová měření, která byla méně citlivá na rychlé změny v rádiovém prostředí na konkrétním místě mobilu. Využitím schopnosti mobilu přímo měřit okolní buňky poskytuje MAHO síti vysoce přesná, reálná a na uživatele zaměřená rádiová data.

Tento přístup řešil klíčová omezení. Umožnil rychlejší a spolehlivější rozhodnutí o předání hovoru, což je klíčové pro obsluhu rychle se pohybujících účastníků a prevenci přerušení hovoru. Také umožnil efektivnější správu síťových zdrojů, neboť centralizovaný [BSC](/mobilnisite/slovnik/bsc/) mohl činit optimalizovaná rozhodnutí na základě globálního pohledu na provoz a rušení, nikoli pouze sílu signálu. Navíc tím, že měření provádí mobil, se síť vyhne významné režii a latenci, která by byla potřeba, aby síť neustále sondovala všechny možné sousední buňky pro každého připojeného uživatele. MAHO se tak stal základním kamenem síťově řízené mobility, vyvažující inteligenci sítě se senzorickými schopnostmi mobilního zařízení.

## Klíčové vlastnosti

- Mobilní stanice provádí měření na kmitočtech BCCH obsluhující a okolních buněk.
- Hlášení o měření jsou periodicky odesílána BSC/RNC prostřednictvím SACCH.
- Síť (BSC/RNC) si ponechává plnou pravomoc pro konečné rozhodnutí o předání hovoru.
- Podporuje předání hovoru na základě úrovně signálu, kvality, vzdálenosti a zatížení provozem.
- Umožňuje plynulá předání hovoru pro mobilní uživatele pohybující se vysokou rychlostí.
- Základ pro síťově řízenou správu mobility v GSM a UMTS.

## Související pojmy

- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding

---

📖 **Anglický originál a plná specifikace:** [MAHO na 3GPP Explorer](https://3gpp-explorer.com/glossary/maho/)

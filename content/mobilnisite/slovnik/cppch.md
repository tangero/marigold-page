---
slug: "cppch"
url: "/mobilnisite/slovnik/cppch/"
type: "slovnik"
title: "CPPCH – Compact Packet Paging Channel"
date: 2025-01-01
abbr: "CPPCH"
fullName: "Compact Packet Paging Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cppch/"
summary: "Compact Packet Paging Channel (CPPCH) je downlinkový logický kanál v sítích GSM/GPRS/EDGE navržený k efektivnímu upozornění mobilních stanic na příchozí paketové datové relace. Optimalizuje kapacitu v"
---

CPPCH je downlinkový logický kanál v sítích GSM/GPRS/EDGE, který využívá kompaktní formát zpráv k efektivnímu vyvolání mobilních stanic pro příchozí paketová data, čímž optimalizuje kapacitu a snižuje signalizační režii.

## Popis

Compact Packet Paging Channel (CPPCH) je základní logický kanál v architektuře rádiového přístupového sítě GSM/[GPRS](/mobilnisite/slovnik/gprs/)/[EDGE](/mobilnisite/slovnik/edge/), fungující na downlinku od subsystému základnové stanice ([BSS](/mobilnisite/slovnik/bss/)) k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). Jak je specifikováno v 3GPP TS 43.064, funguje jako vyhrazený mechanizmus vyvolání pro služby s přepojováním paketů, odlišný od kanálů pro vyvolání s přepojováním okruhů používaných pro hlasové hovory. CPPCH přenáší požadavky na vyvolání specificky pro mobilní stanicí ukončené paketové datové relace, čímž upozorňuje zařízení, že jsou pro příchozí přenos dat alokovány síťové prostředky. Tento kanál funguje v rámci celkové struktury vyvolávacích skupin buňky, kde mobilní stanice monitorují specifické vyvolávací bloky na základě svého International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) nebo Packet-Temporary Mobile Subscriber Identity ([P-TMSI](/mobilnisite/slovnik/p-tmsi/)), aby určily, kdy potřebují naslouchat vyvolávacím zprávám.

Architektonicky je CPPCH mapován na Packet Data Channel ([PDCH](/mobilnisite/slovnik/pdch/)) na fyzické vrstvě, konkrétně v rámci struktury Packet Common Control Channel ([PCCCH](/mobilnisite/slovnik/pccch/)), pokud je dostupný, nebo alternativně na Common Control Channel (CCCH) v buňkách bez PCCCH. Kanál používá specifický formát zprávy – PACKET PAGING REQUEST – který obsahuje základní identifikátory jako P-TMSI nebo IMSI spolu s dalšími informačními elementy, které pomáhají mobilní stanici zpracovat vyvolání efektivně. Kompaktní povaha této zprávy snižuje množství dat, která je třeba přenést, ve srovnání s tradičními přístupy k vyvolání, čímž šetří rádiové prostředky a snižuje latenci při navazování paketových datových relací.

Z provozní perspektivy, když Serving GPRS Support Node (SGSN) obdrží paketová data určená pro mobilní stanici, spustí proceduru vyvolání napříč relevantní směrovací oblastí. BSS obdrží tento požadavek na vyvolání přes rozhraní Gb a naplánuje odpovídající zprávu PACKET PAGING REQUEST na CPPCH během příslušného vyvolávacího bloku pro danou konkrétní mobilní stanici. Mobilní stanice, která se periodicky probouzí ze svého stavu nečinnosti nebo pohotovosti, aby monitorovala své přiřazené vyvolávací bloky, tuto zprávu detekuje a zahájí proceduru žádosti o kanál k založení dočasného toku bloků (Temporary Block Flow, TBF) pro příchozí přenos dat. Celý tento proces je optimalizován tak, aby minimalizoval dobu, po kterou musí být přijímač mobilní stanice aktivní, čímž prodlužuje výdrž baterie a zároveň zajišťuje včasné doručení paketových dat.

CPPCH hraje klíčovou roli v celkových procedurách správy mobility a správy relací pro sítě GPRS/EDGE. Rozhraní s protokoly vyšších vrstev, jako je Logical Link Control (LLC) a Radio Link Control/Medium Access Control (RLC/MAC), koordinuje proces vyvolání. Návrh kanálu podporuje scénáře převzetí buňky řízené sítí i s asistencí mobilní stanice, což zajišťuje, že vyvolávací zprávy dosáhnou mobilních stanic i při jejich pohybu mezi buňkami. Poskytnutím specializovaného, efektivního mechanizmu pro vyvolání paketových dat umožňuje CPPCH škálovatelné nasazení služeb dat v režimu trvalého připojení (always-on) při vyvažování kompromisů mezi kapacitou sítě, signalizační zátěží a spotřebou energie zařízení.

## K čemu slouží

Compact Packet Paging Channel byl vytvořen, aby řešil specifická omezení raných sítí GSM, které byly původně navrženy primárně pro služby hlasu s přepojováním okruhů. Když byl představen GPRS (General Packet Radio Service) pro přidání možností přepojování paketů do sítí GSM, ukázalo se, že stávající mechanizmy vyvolání jsou pro charakter paketového datového provozu neefektivní. Tradiční vyvolání s přepojováním okruhů spotřebovávalo značné signalizační prostředky pro každý pokus o vyvolání, což se stalo problematickým s častějšími, ale menšími událostmi vyvolání charakteristickými pro paketové datové služby jako oznámení e-mailů, instant messaging a prohlížení webu. CPPCH byl vyvinut, aby poskytl optimalizovaný kanál pro vyvolání specificky přizpůsobený požadavkům služeb paketových dat.

Před CPPCH muselo vyvolání paketových dat používat buď stávající kanály pro vyvolání s přepojováním okruhů (které spotřebovávaly cennou kapacitu potřebnou pro hlasové služby), nebo neefektivní řešení, která zvyšovala latenci a snižovala celkovou kapacitu systému. Zprávy pro vyvolání s přepojováním okruhů byly poměrně rozsáhlé a nebyly optimalizované pro typické případy užití paketových dat, kde mohlo být potřeba často vyvolat mnoho zařízení, ale s minimální výměnou dat. To vytvářelo zahlcení na řídicích kanálech a snižovalo počet současných datových uživatelů, které síť mohla efektivně podporovat. CPPCH tyto problémy řeší zavedením kompaktního formátu zpráv, který snižuje režii na každý pokus o vyvolání, umožňuje efektivnější využití rádiových prostředků a podporuje vyšší hustotu uživatelů paketových dat.

Vytvoření CPPCH bylo motivováno potřebou učinit sítě GPRS/EDGE škálovatelnějšími a s lepší odezvou pro vznikající mobilní datové aplikace. Optimalizací procedury vyvolání pro paketové služby mohly sítě podporovat aplikace v režimu trvalého připojení (always-on) bez zahlcení kapacity řídicích kanálů nebo významného dopadu na kvalitu hlasových služeb. To bylo obzvláště důležité, když mobilní operátoři začali nasazovat datové služby pro masového zákazníka, což vyžadovalo efektivní zpracování častých, ale krátkých datových relací. CPPCH také umožnil lepší správu energie pro mobilní zařízení, protože kompaktní formát umožňoval rychlejší zpracování a návrat do režimů úspory energie, čímž prodlužoval výdrž baterie pro datově orientovaná zařízení – což byl klíčový aspekt pro přijetí služeb mobilního internetu.

## Klíčové vlastnosti

- Kompaktní formát zpráv snižující signalizační režii
- Vyhrazené vyvolání pro služby s přepojováním paketů oddělené od vyvolání s přepojováním okruhů
- Mapování na Packet Common Control Channel (PCCCH) nebo Common Control Channel (CCCH)
- Podpora vyvolání založeného na P-TMSI i IMSI
- Optimalizováno pro častá, krátká oznámení o datových relacích
- Vylepšená efektivita baterie díky snížené době aktivity mobilní stanice

## Související pojmy

- [P-TMSI – Packet-Temporary Mobile Subscriber Identity](/mobilnisite/slovnik/p-tmsi/)
- [PCCCH – Packet Common Control Channel](/mobilnisite/slovnik/pccch/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [CPPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cppch/)

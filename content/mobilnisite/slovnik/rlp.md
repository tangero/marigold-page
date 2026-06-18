---
slug: "rlp"
url: "/mobilnisite/slovnik/rlp/"
type: "slovnik"
title: "RLP – Radio Link Protocol"
date: 2025-01-01
abbr: "RLP"
fullName: "Radio Link Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rlp/"
summary: "Protokol linkové vrstvy definovaný v GSM (04.22) pro okruhově spínané datové služby. Poskytuje spolehlivou, uspořádanou službu přenosu dat přes inherentně náchylné k chybám rozhraní rádiového přístupu"
---

RLP je protokol linkové vrstvy pro GSM okruhově spínaná data, který zajišťuje spolehlivý a uspořádaný přenos dat přes rozhraní rádiového přístupu pomocí detekce chyb a retransmisí.

## Popis

Radio Link Protocol (RLP) je protokol vrstvy 2 (linkové vrstvy) specifikovaný v GSM 04.22, navržený pro podporu transparentních a netransparentních okruhově spínaných datových služeb ([CSD](/mobilnisite/slovnik/csd/)) přes rozhraní GSM rádiového přístupu. Funguje mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a funkcí pro propojení sítě ([IWF](/mobilnisite/slovnik/iwf/)) v síti, typicky umístěnou v ústředně mobilní komunikace ([MSC](/mobilnisite/slovnik/msc/)). Primární funkcí RLP je přeměnit náchylný k chybám, syrový rádiový kanál na virtuální spolehlivý datový kanál. Toho dosahuje pomocí rámcové struktury a mechanismu automatického opakování žádosti ([ARQ](/mobilnisite/slovnik/arq/)). Data z vyšší vrstvy jsou segmentována do RLP rámců, z nichž každý obsahuje hlavičku s pořadovými čísly a řídicími informacemi a datovou část. Protokol používá pro opravu chyb schémata ARQ selektivního odmítnutí ([SREJ](/mobilnisite/slovnik/srej/)) a odmítnutí ([REJ](/mobilnisite/slovnik/rej/)). Pokud je rámec přijat s chybou nebo chybí, může přijímač vyžádat retransmisi konkrétních rámců, čímž zajišťuje integritu dat. RLP funguje ve třech režimech: transparentním režimu (kde se nepoužívá ARQ a chyby jsou předávány výše), netransparentním základním režimu (s ARQ) a netransparentním rozšířeném režimu (s většími velikostmi okna a funkcemi pro vyšší propustnost). Protokol řídí řízení toku pomocí svého okenního mechanismu, který omezuje počet nepotvrzených rámců v přenosu. Zahrnuje také procedury pro inicializaci, synchronizaci a ukončení logického spoje. Ačkoli je primárně pro okruhově spínané přenosy, koncepty RLP ovlivnily pozdější protokoly pro paketové přenosy. Jeho fungování je z velké části neviditelné pro koncovou uživatelskou aplikaci, která komunikuje s protokoly vyšších vrstev, jako je [PPP](/mobilnisite/slovnik/ppp/), běžícími nad spojem zřízeným RLP.

## K čemu slouží

RLP byl vytvořen, aby umožnil spolehlivou datovou komunikaci přes rozhraní rádiového přístupu sítě GSM, které je náchylné k útlumu, interferencím a vysokým chybovostem (BER). Před digitálními celulárními systémy byly datové služby nepraktické. Digitální povaha GSM otevřela tuto možnost, ale syrový rádiový kanál byl nevhodný pro aplikace jako fax, vytáčené připojení modemem a rané mobilní datové terminály, které vyžadovaly nízkou chybovost. Protokol to vyřešil implementací robustního mechanismu ARQ na linkové vrstvě, čímž chránil protokoly vyšších vrstev před chybami způsobenými rádiovým přenosem. Řešil omezení čistě transparentního kanálu, který by kvůli zkreslení mnohé datové aplikace znemožnil. RLP byl základním kamenem datových služeb GSM fáze 2+ a umožnil první vlnu mobilních dat před příchodem GPRS a paketového přepínání. Jeho vývoj byl motivován potřebou poskytnout standardizovanou, spolehlivou službu datového přenosu, která by mohla spolupracovat se stávajícím datovým světem PSTN/ISDN, a tím umožnit služby jako okruhově spínaný fax a videotelefonii, jak jsou definovány v 3GPP releasech.

## Klíčové vlastnosti

- Rámcový protokol s číslováním sekvencí pro integritu dat.
- Mechanismy automatického opakování žádosti (ARQ) selektivního odmítnutí (SREJ) a odmítnutí (REJ).
- Funguje v transparentním a netransparentním režimu podle různých požadavků služeb.
- Poskytuje řízení toku pomocí protokolu s posuvným oknem.
- Definuje procedury pro navázání, synchronizaci a uvolnění spoje.
- Podporuje spolupráci s datovými službami PSTN/ISDN prostřednictvím IWF.

## Související pojmy

- [CSD – Circuit Switched Data](/mobilnisite/slovnik/csd/)
- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [IWF – InterWorking Function](/mobilnisite/slovnik/iwf/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 27.007** (Rel-19) — AT Command Set for UE

---

📖 **Anglický originál a plná specifikace:** [RLP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlp/)

---
slug: "acse"
url: "/mobilnisite/slovnik/acse/"
type: "slovnik"
title: "ACSE – Association Control Service Element"
date: 2025-01-01
abbr: "ACSE"
fullName: "Association Control Service Element"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/acse/"
summary: "ACSE je aplikační protokol vrstvy OSI, který navazuje, udržuje a ukončuje asociace mezi aplikačními entitami. Poskytuje spolehlivé řízení spojení pro služby jako SMS a umožňuje bezpečné a uspořádané k"
---

ACSE je aplikační protokol vrstvy OSI, který navazuje, udržuje a ukončuje asociace mezi aplikačními entitami za účelem poskytování spolehlivého řízení spojení v systémech 3GPP.

## Popis

Association Control Service Element (ACSE) je základní protokol v rámci referenčního modelu Open Systems Interconnection ([OSI](/mobilnisite/slovnik/osi/)), který konkrétně funguje na aplikační vrstvě (vrstva 7). V sítích 3GPP slouží ACSE jako základ pro navazování spolehlivých komunikačních relací mezi aplikačními entitami, například mezi centrem služby krátkých zpráv (SMSC) a dalšími síťovými prvky. Funguje tak, že definuje standardizovanou sadu služebních primitiv a jednotek protokolových dat (PDU), které řídí životní cyklus aplikačních asociací, a zajišťuje, že dvě komunikující entity mohou správně zahájit, udržovat a ukončit svá logická spojení.

ACSE pracuje prostřednictvím přesně definované posloupnosti operací. Když aplikace potřebuje komunikovat, ACSE zahájí požadavek A-ASSOCIATE, který zahrnuje parametry jako názvy aplikačního kontextu, autentizační informace a požadavky na kvalitu služby. Příjemní entita odpoví odpovědí A-ASSOCIATE, která asociaci buď přijme, nebo odmítne. Během asociace ACSE poskytuje mechanismy pro udržování spojení prostřednictvím keep-alive funkcí a pro řešení abnormálních stavů. Nakonec, když je komunikace dokončena, ACSE řídí řádné uvolnění asociace prostřednictvím primitiv A-RELEASE, což zajišťuje, že obě strany správně ukončí relaci bez ztráty dat.

Architektura protokolu se skládá z několika klíčových komponent: Stroj asociačního řízení (Association Control Protocol Machine - ACPM), který implementuje stavový automat pro správu asociací; Aplikační kontext (Application Context), který definuje konkrétní používané aplikační služby; a Prezentační kontext (Presentation Context), který řeší problémy reprezentace dat. ACSE také zahrnuje autentizační mechanismy pro ověření identity komunikujících entit a podporuje jak potvrzované (confirmed), tak nepotvrzované (non-confirmed) režimy služby. V implementacích 3GPP ACSE typicky spolupracuje se služebním prvkem vzdálených operací (Remote Operations Service Element - ROSE) za účelem poskytnutí kompletní funkcionality aplikační vrstvy.

V rámci sítí 3GPP hraje ACSE klíčovou roli ve službách, jako je služba krátkých zpráv (SMS), kde řídí asociace mezi SMSC a dalšími síťovými prvky. Zajišťuje spolehlivé doručování SMS zpráv navazováním bezpečných, ověřených spojení mezi komunikujícími entitami. Robustnost protokolu vychází z jeho komplexních schopností zpracování chyb, včetně mechanismů pro detekci a obnovu z komunikačních selhání, správu časových limitů a řešení porušení protokolu. To činí ACSE obzvláště cenným v telekomunikačních prostředích, kde jsou spolehlivost a bezpečnost prvořadé.

## K čemu slouží

ACSE byl vytvořen, aby řešil základní potřebu standardizované správy asociací v distribuovaných aplikacích. Před jeho vývojem aplikační komunikační protokoly postrádaly konzistentní metody pro navazování a udržování logických spojení mezi entitami, což vedlo k problémům s interoperabilitou a nespolehlivými komunikačními relacemi. Protokol vznikl z cíle referenčního modelu [OSI](/mobilnisite/slovnik/osi/) vytvořit komplexní rámec pro propojení otevřených systémů, kde by zařízení různých výrobců mohla bezproblémově komunikovat.

Primární problém, který ACSE řeší, je spolehlivá správa aplikačních asociací v komplexních telekomunikačních sítích. V systémech 3GPP služby jako SMS vyžadují bezpečná, ověřená spojení mezi síťovými prvky, které mohou být od různých výrobců nebo provozovány různými poskytovateli služeb. ACSE poskytuje standardizované mechanismy pro navazování těchto spojení, ověřování identity komunikujících stran, vyjednávání parametrů služby a zajišťování řádného ukončení relací. Tím odstraňuje potřebu proprietárních řešení pro správu spojení a umožňuje skutečnou interoperabilitu v prostředích s více dodavateli.

Historicky byl vývoj ACSE motivován rostoucí složitostí telekomunikačních sítí a rostoucí potřebou standardizovaných protokolů aplikační vrstvy. Jak se sítě vyvíjely z jednoduchých point-to-point spojení na komplexní distribuované systémy, omezení ad-hoc správy spojení se stala zřejmými. ACSE tato omezení řešil poskytnutím komplexního, standardizovaného přístupu k řízení asociací, který mohl být implementován na různých platformách a v různých aplikacích. Jeho zařazení do standardů 3GPP, zejména pro služby SMS, zajistilo, že mobilní sítě mohou poskytovat spolehlivé, interoperabilní služby zasílání zpráv v globálním měřítku.

## Klíčové vlastnosti

- Standardizované navazování asociace pomocí primitiv A-ASSOCIATE
- Spolehlivé mechanismy uvolnění asociace využívající procedury A-RELEASE
- Autentizační schopnosti pro ověření identity komunikujících entit
- Vyjednávání aplikačního kontextu pro zajištění kompatibility služeb
- Komplexní mechanismy detekce chyb a obnovy
- Podpora jak potvrzovaných (confirmed), tak nepotvrzovaných (non-confirmed) režimů služby

## Definující specifikace

- **TS 23.040** (Rel-19) — SMS Technical Realization

---

📖 **Anglický originál a plná specifikace:** [ACSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/acse/)

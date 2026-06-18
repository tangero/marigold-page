---
slug: "p-rnti"
url: "/mobilnisite/slovnik/p-rnti/"
type: "slovnik"
title: "P-RNTI – Paging Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "P-RNTI"
fullName: "Paging Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/p-rnti/"
summary: "Dočasný identifikátor používaný sítí k vyvolání uživatelských zařízení (UE) v režimu nečinnosti (idle) nebo neaktivity (inactive). Je vysílán na PDCCH, aby naznačil přítomnost vyvolávací zprávy na PDS"
---

P-RNTI (Paging Radio Network Temporary Identifier) je dočasný identifikátor, který síť využívá k vyvolání neaktivních nebo spících uživatelských zařízení (UE). Je vysílán na PDCCH, aby signalizoval přítomnost vyvolávací zprávy na PDSCH pro efektivní dosažitelnost.

## Popis

P-RNTI je klíčový identifikátor v rádiových přístupových sítích LTE a NR, speciálně navržený pro procedury vyvolání (paging). Jedná se o pevnou, předdefinovanou hodnotu (FFFE v hexadecimální soustavě), která není přiřazena konkrétnímu UE, ale je společná pro všechna UE v buňce nebo oblasti vyvolání. Jeho primární funkcí je signalizovat prostřednictvím fyzického kanálu pro řízení downlinku ([PDCCH](/mobilnisite/slovnik/pdcch/)), že vyvolávací zpráva je naplánována na fyzickém sdíleném kanálu downlinku ([PDSCH](/mobilnisite/slovnik/pdsch/)) pro konkrétní příležitost vyvolání (paging occasion). Když je UE ve stavu [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_INACTIVE, periodicky se probouzí, aby sledovalo své určené příležitosti vyvolání a hledalo P-RNTI na PDCCH. Pokud je P-RNTI detekováno, UE dekóduje přidružený formát řídicí informace downlinku ([DCI](/mobilnisite/slovnik/dci/)) 1_0 zakódovaný (scrambled) pomocí P-RNTI, který poskytuje přidělení zdrojů pro vlastní vyvolávací zprávu na PDSCH. UE poté přijme a dekóduje vyvolávací zprávu, aby zkontrolovalo, zda je v seznamu uvedena jeho identita (např. [IMSI](/mobilnisite/slovnik/imsi/) nebo [S-TMSI](/mobilnisite/slovnik/s-tmsi/)). Tento dvoukrokový proces (indikace na PDCCH následovaná dekódováním PDSCH) je vysoce efektivní, protože zabraňuje nutnosti dekódovat celý kanál PDSCH během každé příležitosti vyvolání, čímž výrazně šetří energii baterie. P-RNTI je nedílnou součástí schopnosti sítě iniciovat služby ukončené na mobilní straně (mobile-terminated), jako jsou příchozí hovory nebo datové relace, a upozorňovat UE na změny systémových informací nebo na výstrahy ETWS/[CMAS](/mobilnisite/slovnik/cmas/). Jeho fungování je úzce spojeno s cyklem nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)) UE a s výpočtem rámců vyvolání (paging frames) a příležitostí vyvolání (paging occasions) sítí na základě identit UE.

## K čemu slouží

P-RNTI bylo zavedeno, aby vyřešilo základní problém síťově iniciované dosažitelnosti pro UE, která nejsou v aktivním spojení (RRC_CONNECTED). Před existencí takových mechanismů by udržení neustálé dosažitelnosti vyžadovalo, aby UE nepřetržitě sledovalo downlinkové kanály, což by vedlo k nepřijatelnému vybíjení baterie. P-RNTI umožňuje efektivní mechanismus vyvolání, který je klíčový pro úsporu energie v mobilních zařízeních. Umožňuje síti kontaktovat konkrétní UE nebo skupinu UE pouze v předem určených, nepříliš častých intervalech (příležitostech vyvolání), zatímco UE může po většinu času zůstat v nízkopříkonovém spánkovém stavu. Tento návrh je základním kamenem standardů mobilního širokopásmového připojení, umožňujícím uživatelům vjem stálého připojení bez související neustálé spotřeby energie. Řeší také omezení spočívající v nutnosti znát přesnou polohu buňky, ve které se UE nachází; vyvolávací zpráva může být vysílána do více buněk v rámci oblasti sledování (Tracking Area) v LTE nebo oblasti oznámení RAN (RAN Notification Area) v NR, což usnadňuje správu mobility v režimu nečinnosti.

## Klíčové vlastnosti

- Pevný, společný identifikátor (hodnota FFFE) používaný všemi UE v buňce pro detekci vyvolání.
- Zakóduje (scramble) řídicí informaci downlinku (DCI) na PDCCH, aby signalizoval přítomnost vyvolávací zprávy.
- Umožňuje úsporu energie UE prostřednictvím DRX, protože UE dekóduje PDCCH pro P-RNTI pouze v určitých příležitostech vyvolání.
- Spustí proces, při kterém UE dekóduje následnou vyvolávací zprávu na PDSCH, aby našlo svou konkrétní identitu.
- Používá se pro navázání hovoru ukončeného na mobilní straně, zahájení datové relace a oznámení o změnách systémových informací.
- Podporuje výstražná hlášení veřejnosti ETWS (Earthquake and Tsunami Warning System) a CMAS (Commercial Mobile Alert System).

## Související pojmy

- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)
- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [P-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-rnti/)

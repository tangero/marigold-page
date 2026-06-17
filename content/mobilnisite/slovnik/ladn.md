---
slug: "ladn"
url: "/mobilnisite/slovnik/ladn/"
type: "slovnik"
title: "LADN – Local Area Data Network"
date: 2026-01-01
abbr: "LADN"
fullName: "Local Area Data Network"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ladn/"
summary: "Služba 5G, která poskytuje připojení ke konkrétní datové síti pouze tehdy, když se UE nachází v definované geografické oblasti. Umožňuje efektivní lokalizované datové služby, jako je automatizace výro"
---

LADN je služba 5G, která poskytuje připojení ke konkrétní datové síti pouze tehdy, když se uživatelské zařízení nachází v definované geografické oblasti.

## Popis

Local Area Data Network (LADN) je funkce systému 5G definovaná od 3GPP Release 15. Umožňuje poskytování datové sítě ([DN](/mobilnisite/slovnik/dn/)), která je přístupná uživatelskému zařízení (UE) pouze tehdy, když se UE nachází v konkrétní geografické oblasti, známé jako oblast služby LADN. Toto je klíčový prvek pro lokalizované služby, jako jsou privátní sítě, průmyslový IoT a kampusové sítě. Jádro sítě, konkrétně funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)), je zodpovědné za správu registrace UE a kontextu zřizování relací s ohledem na dostupnost LADN. Když se UE registruje v síti, AMF mu poskytne seznam nakonfigurovaných LADN a jim odpovídajících oblastí služeb. UE tyto informace využívá k určení své způsobilosti přistupovat ke konkrétní LADN na základě své aktuální polohy.

Architektura zahrnuje AMF, funkci správy relací ([SMF](/mobilnisite/slovnik/smf/)) a funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)). AMF ukládá konfiguraci LADN, včetně názvu datové sítě ([DNN](/mobilnisite/slovnik/dnn/)) a přidružené oblasti služeb, která je definována jako sada sledovacích oblastí (TA). Když UE zahájí žádost o zřízení relace PDU pro LADN DNN, AMF zkontroluje hlášenou polohu UE vůči oblasti služby LADN. Pokud je UE mimo tuto oblast, AMF žádost o zřízení relace zamítne, čímž zabrání zbytečné alokaci zdrojů a signalizaci. Pokud je uvnitř, žádost je předána SMF, která pokračuje standardními postupy zřizování relace PDU, případně s výběrem UPF, které jsou pro danou LADN lokální, pro optimální směrování.

LADN funguje díky integraci povědomí o poloze do logiky správy relací v jádru sítě. UE není povinno nepřetržitě sledovat svou polohu pro účely LADN; místo toho spoléhá na aktualizace registrační oblasti od sítě a na znalosti AMF. Oblast služby je nakonfigurována v síti a poskytnuta UE prostřednictvím signalizace ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)). Tento mechanismus zajišťuje, že relace PDU pro LADN jsou aktivní pouze tehdy, když se UE nachází v určené zóně, a jsou deaktivovány nebo se stávají nedostupnými, když UE tuto zónu opustí. Tento model podporuje efektivní síťové krájení (network slicing) pro lokalizované služby, protože instance síťového řezu může být asociována s konkrétní LADN, což zajišťuje využití zdrojů pouze tam, kde je to potřeba.

Klíčové komponenty zahrnují LADN DNN, což je speciální identifikátor DNN, a definici oblasti služby LADN. Role AMF je ústřední, protože provádí autorizační kontrolu. SMF je zodpovědná za správu kontextu relace PDU a za interakci s funkcí řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a UPF. Z pohledu UE povědomí o LADN zahrnuje uložení přijatých informací o oblasti služeb a jejich použití pro podmíněný pokus o zřízení relace PDU. Tato funkce je klíčová pro umožnění 5G podporovat aplikace vertikálních odvětví, které vyžadují ohraničené připojení s nízkou latencí v rámci vymezené geografické oblasti bez dopadu na širší veřejnou síť.

## K čemu slouží

LADN byl vytvořen pro řešení potřeby efektivních, geograficky omezených datových služeb v sítích 5G. Před 5G vyžadovalo poskytování lokalizovaného síťového přístupu (jako je privátní firemní síť) často zastřešující síťové konfigurace nebo vyhrazenou infrastrukturu, která nebyla těsně integrována s mobilním jádrem. To mohlo vést k neefektivnímu využití zdrojů jádra sítě, protože relace mohly být udržovány i když byl uživatel daleko od místa služby, což způsobovalo zbytečnou signalizaci a provoz v uživatelské rovině napříč sítí.

Motivace vychází z vize 5G podporovat rozmanitá vertikální odvětví, jako jsou chytré továrny, přístavy a kampusy. Tato prostředí vyžadují garantované, vysoce výkonné připojení, které je logicky i fyzicky omezeno na konkrétní oblast. LADN to řeší tím, že činí samotné jádro sítě citlivé na oblast, což mu umožňuje dynamicky povolovat nebo odmítat přístup ke konkrétní datové síti na základě aktuální polohy uživatele. Tím se řeší problém rozprostření síťových zdrojů a umožňuje skutečné síťové krájení pro lokalizované služby, kde jsou zdroje řezu spotřebovávány pouze tehdy, když je uživatel fyzicky přítomen v příslušné oblasti. Poskytuje standardizovanou, v jádru sítě nativní metodu pro omezení oblasti služby, což představuje posun oproti starším, méně efektivním metodám, jako je řízení přístupu na základě buněk nebo překryvné sítě.

## Klíčové vlastnosti

- Geograficky omezený přístup ke konkrétní datové síti (DN)
- Oblast služby definována jako sada sledovacích oblastí (TA)
- UE obdrží konfiguraci LADN během registrace
- AMF provádí autorizaci založenou na poloze pro zřízení relace PDU
- Umožňuje efektivní využití zdrojů pro lokalizované/privátní síťové služby
- Podporuje integraci se síťovým krájením 5G pro aplikace vertikálních odvětví

## Související pojmy

- [DNN – Data Network Name](/mobilnisite/slovnik/dnn/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TR 33.839** (Rel-17) — Edge Computing Security Study for 5G Core

---

📖 **Anglický originál a plná specifikace:** [LADN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ladn/)

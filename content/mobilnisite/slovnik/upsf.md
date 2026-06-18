---
slug: "upsf"
url: "/mobilnisite/slovnik/upsf/"
type: "slovnik"
title: "UPSF – User Profile Server Function"
date: 2025-01-01
abbr: "UPSF"
fullName: "User Profile Server Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/upsf/"
summary: "Síťová funkce, která ukládá a spravuje uživatelsky orientovaná data (předplatné, preference, zásady) pro poskytování služeb. Působí jako jednotné datové úložiště, které umožňuje personalizované služby"
---

UPSF (User Profile Server Function) je síťová funkce, která ukládá a spravuje uživatelsky orientovaná data, jako jsou informace o předplatném a zásadách, a slouží jako jednotné datové úložiště pro umožnění personalizovaných služeb napříč různými síťovými doménami.

## Popis

User Profile Server Function (UPSF) je standardizovaná síťová funkce, která slouží jako centrální úložiště pro data související s uživatelem. Původně definovaná v kontextu IP Multimedia Subsystem (IMS) pro konvergenci pevných a mobilních sítí se její role rozšířila do architektury 5G jádra. UPSF ukládá komplexní uživatelský profil, který přesahuje základní informace o předplatném. Tento profil typicky zahrnuje uživatelské identity, data o předplatném služeb, preference, zásady a případně data specifická pro aplikace. Je definována v několika specifikacích 3GPP, včetně TS 23.417 ([FMC](/mobilnisite/slovnik/fmc/)), 23.517 (architektura 5G) a specifikací pro správu TS 32.808.

Architektonicky je UPSF logická entita, která může být implementována jako samostatný síťový prvek nebo integrována s jinými funkcemi, jako je Unified Data Repository ([UDR](/mobilnisite/slovnik/udr/)) v 5G. Svá data zpřístupňuje prostřednictvím standardizovaných rozhraní, především rozhraní Sh v IMS (směrem k aplikačním serverům a [S-CSCF](/mobilnisite/slovnik/s-cscf/)) a služebního rozhraní Nudr v 5G (směrem k funkcím jako [PCF](/mobilnisite/slovnik/pcf/), [NEF](/mobilnisite/slovnik/nef/) a [UDM](/mobilnisite/slovnik/udm/)). UPSF tato data nezpracovává ani na jejich základě neprovádí logiku; místo toho poskytuje spolehlivé služby ukládání, načítání a oznamování. Ostatní síťové funkce dotazují UPSF, aby získaly uživatelská data potřebná pro poskytování služeb, řízení relací nebo rozhodování o zásadách.

UPSF funguje na základě modelu oznámení založeného na předplatném. Autorizovaná síťová funkce se může přihlásit k odběru oznámení o změně konkrétních dat v uživatelském profilu. Například pokud je uživatelská servisní politika aktualizována prostřednictvím administrativního nástroje, UPSF může odeslat oznámení přihlášenému PCF, který pak může spustit aktualizaci politiky UE. Tento push mechanismus zajišťuje konzistenci v síti. V 5G koncept UPSF koresponduje se strukturovaným úložištěm dat UDR, kde jsou uživatelská data organizována do datových sad (např. data předplatného, data zásad, aplikační data). UPSF lze chápat jako implementaci specifických datových sad, poskytující jednotný pohled na uživatelské informace, který je klíčový pro umožnění personalizovaných a konzistentních služeb napříč přístupovými technologiemi a servisními doménami.

## K čemu slouží

UPSF byla vytvořena k řešení problému fragmentovaných a izolovaných uživatelských dat v telekomunikačních sítích. Historicky byly uživatelské informace duplikovány napříč více síťovými prvky ([HLR](/mobilnisite/slovnik/hlr/), [HSS](/mobilnisite/slovnik/hss/), aplikační servery), což vedlo k nekonzistenci, složitému zřizování a neschopnosti nabízet jednotné služby. Snaha o konvergenci pevných a mobilních sítí (FMC) ve vydání 7 zdůraznila potřebu jediného, sdíleného úložiště pro uživatelské profily, které by mohlo být přístupné jak službám založeným na IMS, tak i dalším síťovým doménám.

Jejím účelem je centralizovat uživatelsky orientovaná data, čímž se zjednodušuje síťová architektura, zlepšuje se konzistence dat a umožňují se pokročilé personalizované služby. Poskytnutím standardizovaného úložiště a přístupového bodu umožňuje UPSF servisní logice (v aplikačních serverech) a řídicí logice (v CSCF, PCF) využívat stejnou sadu uživatelských preferencí a zásad. Toto byl základní krok k datově orientované architektuře plně realizované v 5G s UDR. UPSF řeší omezení předchozích přístupů oddělením úložiště dat od řídicích funkcí, což umožňuje flexibilnější nasazení služeb, efektivnější správu dat a podporu přístupu aplikací třetích stran prostřednictvím vystavených API.

## Klíčové vlastnosti

- Centralizované úložiště pro uživatelská data o předplatném, preferencích a zásadách
- Podporuje standardizovaná přístupová rozhraní (např. Sh v IMS, Nudr v 5G)
- Umožňuje mechanismy předplatného/oznamování pro upozornění na změny dat
- Usnadňuje konvergenci pevných a mobilních sítí (FMC) a konzistentní uživatelský zážitek
- Soulad s architekturou 5G UDR, správa specifických uživatelských datových sad
- Odděluje úložiště dat od síťové řídicí logiky pro flexibilitu

## Související pojmy

- [UDR – Unified Data Repository](/mobilnisite/slovnik/udr/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 29.433** (Rel-8) — ETSI TISPAN Endorsement of 3GPP Cx/Dx Interfaces
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [UPSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/upsf/)

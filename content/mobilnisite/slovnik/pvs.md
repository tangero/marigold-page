---
slug: "pvs"
url: "/mobilnisite/slovnik/pvs/"
type: "slovnik"
title: "PVS – Provisioning Server"
date: 2026-01-01
abbr: "PVS"
fullName: "Provisioning Server"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pvs/"
summary: "Provisioning Server (PVS) je síťová funkce v systémech 5G odpovědná za bezpečné doručování konfiguračních dat, zásad a servisních parametrů uživatelskému zařízení (UE). Umožňuje vzdálenou správu zaříz"
---

PVS je síťová funkce 5G, která bezpečně doručuje konfigurační data, zásady a servisní parametry uživatelskému zařízení (UE) pro vzdálenou správu a provizionování.

## Popis

Provisioning Server (PVS) je standardizovaná síťová funkce zavedená v architektuře 5G System (5GS), která funguje v rámci rámce pro správu a umožnění. Jejím hlavním úkolem je bezpečné, spolehlivé a efektivní doručování provizionovacích informací uživatelskému zařízení (UE). Tyto informace jsou rozmanité a mohou zahrnovat počáteční bootstrapovou konfiguraci pro zařízení (zvláště klíčovou pro IoT), parametry zásad, servisně orientovaná konfigurační data, aktualizace pro aplikace na UE a parametry pro výběr síťového řezu. PVS komunikuje s dalšími síťovými funkcemi 5G jádra a externími entitami, jako jsou aplikační servery nebo platformy pro správu zařízení.

Z architektonického hlediska je PVS definován jako aplikační server, který komunikuje s UE prostřednictvím 5G jádrové sítě. Klíčovým protokolem pro tuto komunikaci je Provisioning Protocol, který může být založen na [HTTPS](/mobilnisite/slovnik/https/) nebo CoAP pro omezená IoT zařízení. UE objevuje a připojuje se k PVS pomocí informací, které mohou být předkonfigurované, odvozené z karty UICC nebo poskytnuté sítí během registrace (např. prostřednictvím [UDM](/mobilnisite/slovnik/udm/) nebo [PCF](/mobilnisite/slovnik/pcf/)). 5G jádrová síť, konkrétně Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)), často funguje jako zprostředkovatel nebo umožňovatel, poskytuje bezpečné rozhraní založené na [API](/mobilnisite/slovnik/api/), přes které mohou externí Application Functions ([AF](/mobilnisite/slovnik/af/)) požadovat doručení provizionovacích dat konkrétním UE prostřednictvím PVS.

Provizionovací proces typicky zahrnuje několik kroků. Nejprve UE spustí provizionování, často při počátečním zapnutí nebo na základě zásady. Naváže bezpečné spojení (např. [TLS](/mobilnisite/slovnik/tls/)/[DTLS](/mobilnisite/slovnik/dtls/)) s PVS, autentizované pomocí přihlašovacích údajů 5G. PVS, který mohl obdržet provizionovací instrukce od externího systému správy, poté doručí strukturovaný datový balíček (např. JSON objekt) do UE. Provizionovací klient v UE tato data zpracuje a aplikuje konfiguraci na příslušné podsystémy (např. aktualizuje zásady konektivity, nakonfiguruje aplikaci nebo uloží servisní parametry). PVS podporuje jak push, tak pull modely doručování dat a umí zpracovávat potvrzení a hlášení chyb, čímž zajišťuje, že provizionovací transakce je dokončena a úspěšná.

## K čemu slouží

PVS byl vytvořen k řešení kritické potřeby škálovatelného, automatizovaného a bezpečného vzdáleného provizionování zařízení v 5G, systému navrženém pro podporu obrovského počtu různorodých zařízení od chytrých telefonů po masivní IoT senzory. Tradiční manuální provizionování nebo protokoly pro správu specifické pro zařízení byly pro tento rozsah a heterogenitu nedostatečné. PVS poskytuje jednotný, standardy založený mechanismus v rámci architektury 5G.

Řeší několik klíčových problémů. Za prvé umožňuje provizionování IoT zařízení bez nutnosti zásahu (zero-touch), což jim umožňuje být nasazena v terénu a automaticky přijímat svou provozní konfiguraci ze sítě, což drasticky snižuje provozní náklady. Za druhé umožňuje dynamické aktualizace zásad a servisních parametrů bez nutnosti kompletní aktualizace firmwaru zařízení nebo zásahu uživatele, což umožňuje flexibilní poskytování služeb. Za třetí poskytuje bezpečný kanál pro doručování citlivých konfiguračních dat s využitím robustního rámce pro autentizaci a zabezpečení 5G. Jeho zavedení bylo motivováno vizí síťových řezů a servisně orientované architektury, kde může být konfigurace zařízení potřebná přizpůsobit pro konkrétní síťové řezy nebo aplikace za běhu. PVS je základním umožňovatelem efektivního řízení životního cyklu zařízení v éře 5G.

## Klíčové vlastnosti

- Bezpečně doručuje konfigurační data a data zásad do UE přes 5G sítě
- Podporuje bootstrapové provizionování pro IoT zařízení (nasazení bez nutnosti zásahu)
- Umožňuje dynamické aktualizace dat specifických pro aplikace a servisních parametrů
- Může být přístupný externím Application Functions prostřednictvím NEF pro cílené provizionování
- Využívá provizionovací protokoly založené na HTTPS nebo CoAP vhodné pro různorodá zařízení
- Integruje se s autentizačními a bezpečnostními mechanismy 5G pro důvěryhodné doručování dat

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification

---

📖 **Anglický originál a plná specifikace:** [PVS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pvs/)

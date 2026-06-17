---
slug: "adm"
url: "/mobilnisite/slovnik/adm/"
type: "slovnik"
title: "ADM – Administrative Access Condition"
date: 2026-01-01
abbr: "ADM"
fullName: "Administrative Access Condition"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/adm/"
summary: "ADM (Administrative Access Condition) je bezpečnostní mechanismus v aplikacích UICC/USIM, který řídí přístup k elementárním souborům (EFs). Představuje nejvyšší úroveň oprávnění, kdy přístup k souboru"
---

ADM je podmínka administrativního přístupu s nejvyššími oprávněními v UICC/USIM, která řídí přístup k souborům a zajišťuje, že kritická data účastníka a síťové parametry zůstanou chráněny operátorem, který je vytvořil.

## Popis

ADM (Administrative Access Condition) je základní bezpečnostní koncept ve specifikacích 3GPP pro aplikace Universal Integrated Circuit Card (UICC) a Universal Subscriber Identity Module (USIM). Funguje jako příznak nebo podmínka řízení přístupu přidružená ke konkrétním elementárním souborům (EFs) uloženým na čipové kartě. K EF označenému ADM může přistupovat (pro čtení, aktualizaci nebo mazání) pouze entita disponující správným ADM klíčem nebo přihlašovacími údaji, které výhradně vlastní administrativní autorita – obvykle mobilní síťový operátor (MNO) nebo poskytovatel služeb, který UICC vytvořil a personalizoval.

Mechanismus funguje v rámci bezpečnostní architektury UICC, která zahrnuje hierarchii přístupových podmínek: ALWays (volný přístup), NEVer (žádný přístup), CHV (ověření držitele karty pomocí PINu) a ADM. ADM stojí na vrcholu této hierarchie a poskytuje nejsilnější ochranu. Když se aplikace v terminálu (Mobile Equipment) pokusí přistoupit k EF, operační systém UICC zkontroluje přístupové podmínky souboru. Pokud je nastaven ADM, musí terminál předložit platné ověření pomocí ADM klíče, typicky prostřednictvím zabezpečeného kanálu navázaného s kartou. Tento proces často zahrnuje kryptografické výzvy a odpovědi k prokázání držení klíče bez jeho odhalení.

Klíčové komponenty zapojené do vynucování ADM zahrnují deskriptor souboru EF (který uchovává přístupovou podmínku), správce zabezpečení UICC a autentizační algoritmy. Podmínka ADM je definována během fáze personalizace karty a je klíčová pro ochranu citlivých souborů, jako jsou ty obsahující přihlašovací údaje pro síťový přístup (např. IMSI), parametry služeb specifické pro operátora a seznamy pro roaming. Administrativní autorita využívá ADM k udržení kontroly nad těmito kritickými parametry, což zajišťuje, že mohou být bezpečně aktualizovány přes vzdušné rozhraní (OTA) nebo při fyzické údržbě, a zároveň brání jejich neoprávněné manipulaci ze strany koncových uživatelů nebo neautorizovaných aplikací.

V širší síťové architektuře ADM podporuje bezpečnou správu předplatného a poskytování služeb. Operátorům umožňuje vzdáleně spravovat obsah UICC prostřednictvím OTA platforem pomocí ověření ADM klíči. To je zásadní pro moderní profily eSIM (eUICC) a nasazení IoT, kde je vzdálená správa prvořadá. Integrita mechanismu ADM je základem důvěry v modul identifikace účastníka, protože jeho narušení by mohlo vést k neoprávněnému přístupu do sítě nebo krádeži služeb. ADM klíče proto patří mezi nejpřísněji střežená tajemství v bezpečnostní infrastruktuře operátora a jsou často spravovány pomocí Hardware Security Modules (HSMs) v zabezpečených provisioningových centrech.

## K čemu slouží

ADM bylo vytvořeno pro uspokojení kritické potřeby mobilních síťových operátorů udržovat výhradní administrativní kontrolu nad citlivými daty uloženými na modulech identifikace účastníka. V raných systémech GSM, jak se čipové karty vyvíjely z jednoduchých autentizačních tokenů na komplexní platformy služeb, potřebovali operátoři mechanismus k ochraně síťově specifických souborů před neoprávněným přístupem – ať už ze strany koncových uživatelů, aplikací třetích stran nebo útočníků. Bez ADM by operátoři nemohli bezpečně aktualizovat klíčové parametry, jako je IMSI, kryptografické klíče nebo nastavení služeb, což by ohrozilo zabezpečení sítě a integritu služeb.

Zavedení ADM ve 3GPP Release 5 formalizovalo tuto nejvyšší úroveň řízení přístupu v rámci standardizovaného bezpečnostního rámce pro aplikace UICC/USIM. Vyřešilo tak omezení dřívějších, primitivnějších přístupových kontrol, kterým chyběla jasná hierarchie pro administrativní oprávnění. Definováním ADM jako samostatné podmínky umožnilo 3GPP operátorům delegovat některé uživatelsky přístupné funkce (prostřednictvím CHV/PINu), a přitom si ponechat konečnou autoritu nad kritickými soubory. Toto oddělení kompetencí je zásadní pro moderní správu předplatného, protože umožňuje uživatelům personalizovat některé aspekty (jako telefonní seznamy), a zároveň zajišťuje, že data kritická pro síť zůstávají pod kontrolou operátora.

Historicky bylo vytvoření ADM motivováno rostoucí komplexitou mobilních služeb a přechodem k OTA aktualizacím. Jak operátoři začali nasazovat služby s přidanou hodnotou a potřebovali vzdáleně spravovat předplatná, stal se robustní mechanismus administrativního přístupu nezbytným. ADM poskytlo technický základ pro zabezpečené OTA platformy, což umožnilo důvěryhodnou správu služeb bez fyzického přístupu ke kartě. Tato schopnost se stala ještě důležitější s nástupem eSIM a IoT, kde je vzdálená provize a správa životního cyklu standardním požadavkem, čímž se ADM stalo pilířem současných architektur mobilní bezpečnosti.

## Klíčové vlastnosti

- Řízení přístupu s nejvyššími oprávněními pro elementární soubory UICC/USIM
- Výhradní správa autoritou, která soubor vytvořila (typicky MNO)
- Umožňuje zabezpečené aktualizace kritických parametrů přes vzdušné rozhraní (OTA)
- Integruje se s bezpečnostní architekturou UICC a autentizačními protokoly
- Chrání citlivá data jako IMSI, kryptografické klíče a nastavení operátora
- Podporuje vzdálenou správu předplatného pro nasazení eSIM a IoT

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.369** (Rel-19) — 5G System Architecture for Ambient IoT
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 28.540** (Rel-20) — 5G Network Resource Model (NRM) Management
- **TS 29.504** (Rel-19) — Nudr Service Based Interface Stage 3 Protocol
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 32.181** (Rel-19) — User Data Convergence Management Framework
- **TR 32.901** (Rel-19) — UDC Application Data Models Study
- **TS 33.369** (Rel-19) — Security for AIoT in Isolated Private 5G Networks
- **TS 33.713** (Rel-19) — Security Study for Ambient IoT in 5G
- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [ADM na 3GPP Explorer](https://3gpp-explorer.com/glossary/adm/)

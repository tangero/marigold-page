---
slug: "add"
url: "/mobilnisite/slovnik/add/"
type: "slovnik"
title: "ADD – Automatic Device Detection"
date: 2025-01-01
abbr: "ADD"
fullName: "Automatic Device Detection"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/add/"
summary: "ADD je mechanismus 3GPP pro automatické detekování a registraci uživatelského zařízení (UE) při jeho připojení k mobilní síti. Umožňuje síti identifikovat schopnosti zařízení a spustit odpovídající po"
---

ADD je mechanismus 3GPP pro automatické detekování a registraci uživatelského zařízení při jeho připojení k mobilní síti, umožňující identifikaci zařízení a poskytování služeb bez manuálního zásahu.

## Popis

Automatic Device Detection (ADD) je standardizovaná funkce správy sítě definovaná 3GPP, která umožňuje páteřní síti automaticky rozpoznat a zaregistrovat uživatelské zařízení (UE) při jeho počátečním připojení nebo při přístupu ke službám. Funguje primárně v doméně paketového přepojování (PS), přičemž komunikuje se síťovými uzly, jako je Serving GPRS Support Node (SGSN) ve starších vydáních, a Mobility Management Entity (MME) a Packet Data Network Gateway (PGW) v pozdějších architekturách Evolved Packet Core (EPC). Proces je zahájen, když se UE pokouší navázat datovou relaci; síť zachytí požadavek na připojení a extrahuje informace specifické pro zařízení, jako je International Mobile Equipment Identity (IMEI) nebo jiné identifikátory, které jsou následně použity k dotazu na centrální databázi zařízení nebo k provedení lokální logiky pro určení typu zařízení a jeho schopností.

Architektura zahrnuje několik klíčových komponent: samotné UE, které poskytuje svou identitu; řídicí uzly páteřní sítě (SGSN/MME), které zařízení detekují během procedur připojování; a často externí Device Identity Register (DIR) nebo integrace s Equipment Identity Register (EIR). Ve své činnosti ADD využívá stávající signalizační protokoly, jako je GPRS Tunneling Protocol (GTP) v rozhraních Gn/Gp nebo Diameter v rozhraních S6a/S6d, ke komunikaci informací o zařízení. Když se UE připojí, SGSN nebo MME může spustit ADD proceduru odesláním požadavku na kontrolu zařízení určené síťové funkci, která analyzuje identifikátor a vrátí profil udávající model zařízení, podporované funkce (např. technologie rádiového přístupu, parametry QoS) a případná omezení služeb.

ADD hraje klíčovou roli v řízení sítě tím, že umožňuje automatizované vynucování politik, diferenciaci služeb a optimalizaci zdrojů. Například po detekci konkrétního typu zařízení může síť uplatnit přizpůsobená nastavení QoS, přidělit odpovídající přenašeče nebo omezit přístup na základě předplatného nebo schopností. Tím se snižují chyby způsobené manuální konfigurací a operátoři mohou dynamicky přizpůsobovat rozmanitým ekosystémům zařízení, od chytrých telefonů po IoT senzory. V pozdějších vydáních 3GPP bylo ADD integrováno s rámci pro řízení politik, jako je PCRF (Policy and Charging Rules Function), aby umožnilo poskytování služeb v reálném čase s ohledem na zařízení, čímž se zvyšuje efektivita sítě a spokojenost uživatelů.

## K čemu slouží

ADD bylo zavedeno ve vydání 3GPP Release 5, aby řešilo rostoucí složitost mobilních sítí v souvislosti s narůstající diverzitou zařízení s příchodem GPRS a UMTS. Před zavedením ADD se síťoví operátoři často spoléhali na manuální konfiguraci nebo statické poskytování služeb pro správu služeb specifických pro zařízení, což bylo neefektivní a náchylné k chybám, zejména s rozšířením datově schopných zařízení. Manuální přístup se nedokázal škálovat pro zvládání milionů připojení, což vedlo k nekonzistentnosti služeb a zvýšeným provozním nákladům. ADD tento proces automatizovalo, což umožnilo sítím dynamicky identifikovat zařízení a uplatňovat odpovídající politiky, čímž se vyřešily problémy související s aktivací služeb, prevencí podvodů a přidělováním zdrojů.

Historický kontext pro ADD zahrnuje expanzi služeb mobilního internetu, kde operátoři potřebovali rozlišovat mezi typy zařízení (např. feature telefony vs. chytré telefony), aby mohli nabízet přizpůsobené datové tarify a zajistit síťovou kompatibilitu. Omezení předchozích přístupů zahrnovala nedostatek detekce v reálném čase, což bránilo optimálnímu řízení QoS a mohlo způsobit zahlcení sítě špatně nakonfigurovanými zařízeními. ADD poskytlo standardizovaný způsob automatické detekce zařízení, což umožnilo operátorům implementovat účtování s ohledem na zařízení, bezpečnostní opatření (jako je blokování ukradených zařízení prostřednictvím integrace s EIR) a efektivní využití síťových zdrojů. To bylo motivováno potřebou provozní automatizace a vylepšeného uživatelského zážitku ve vyvíjejících se sítích 3G/4G.

## Klíčové vlastnosti

- Automatická identifikace UE při připojení k síti
- Integrace s EIR pro ověření zařízení a bezpečnost
- Dynamické vynucování politik na základě schopností zařízení
- Podpora diferenciace QoS podle typu zařízení
- Snížení manuální konfigurace a provozní zátěže
- Škálovatelnost pro zvládnutí rozmanitých IoT a spotřebitelských zařízení

## Definující specifikace

- **TS 23.012** (Rel-19) — Circuit Switched Location Management Procedures
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TR 23.702** (Rel-14) — Study on 3GPP PS Data Off
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1

---

📖 **Anglický originál a plná specifikace:** [ADD na 3GPP Explorer](https://3gpp-explorer.com/glossary/add/)

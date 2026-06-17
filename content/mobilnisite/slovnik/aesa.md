---
slug: "aesa"
url: "/mobilnisite/slovnik/aesa/"
type: "slovnik"
title: "AESA – ATM End System Address"
date: 2025-01-01
abbr: "AESA"
fullName: "ATM End System Address"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aesa/"
summary: "AESA je jedinečná síťová adresa pro koncový systém ATM (Asynchronous Transfer Mode), jako je síťový uzel nebo terminál. Používá se pro směrování a identifikaci koncových bodů v transportní síti založe"
---

AESA je jedinečná síťová adresa pro koncový systém ATM, používaná pro směrování a identifikaci koncových bodů v transportní síti založené na ATM.

## Popis

[ATM](/mobilnisite/slovnik/atm/) End System Address (AESA) je klíčový identifikátor adresování v sítích Asynchronous Transfer Mode (ATM), které sloužily jako primární transportní technologie pro rané verze 3GPP (od R99 až po Rel-7 a dále pro některá starší rozhraní). AESA jednoznačně identifikuje koncový bod ATM – například síťový přepínač, směrovač nebo konkrétní rozhraní na síťovém prvku, jako je Radio Network Controller (RNC), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) nebo Gateway GPRS Support Node (GGSN). Funguje podobně jako IP adresa v IP sítích, ale je přizpůsobena spojením orientovanému paradigmatu ATM založenému na virtuálních okruzích. Adresa se používá při nastavování Permanent Virtual Circuits (PVC) nebo Switched Virtual Circuits (SVC) k vytvoření komunikační cesty mezi dvěma koncovými body. Mezi klíčové protokoly využívající AESA patří ATM Adaptation Layer ([AAL](/mobilnisite/slovnik/aal/)), zejména [AAL2](/mobilnisite/slovnik/aal2/) a [AAL5](/mobilnisite/slovnik/aal5/), které jsou specifikovány pro transport uživatelské a řídicí roviny v 3GPP specifikacích jako 25.414 a 25.426.

Z architektonického hlediska je AESA nedílnou součástí zásobníku protokolů ATM a funguje na síťové vrstvě (odpovídá vrstvě 3 v modelu [OSI](/mobilnisite/slovnik/osi/)). Používá se spolu s routovacím protokolem Private Network-Network Interface (PNNI) od fóra ATM nebo se statickou konfigurací pro směrování signalizačních zpráv a uživatelských dat. V kontextu 3GPP se AESA používá na klíčových rozhraních, jako je Iu (mezi RNC a jádrem sítě), Iur (mezi RNC) a Iub (mezi RNC a Node B), stejně jako na rozhraní Gn mezi SGSN a GGSN, když je použit ATM transport. Struktura adresy obvykle odpovídá formátu [ITU-T](/mobilnisite/slovnik/itu-t/) E.164 nebo formátu Network Service Access Point (NSAP) od fóra ATM, který zahrnuje pole pro identifikátor autority a formátu, počáteční doménovou část a část specifickou pro doménu, což umožňuje hierarchické adresování a škálovatelnost.

Úlohou AESA v síti je umožnit přesnou identifikaci koncového bodu a směrování v rámci ATM cloudu. Při navazování spojení signalizační protokoly jako Q.2931 nebo signalizace UNI od fóra ATM používají cílovou AESA k určení cesty přes přepínače ATM sítě. To zajišťuje, že Virtual Channel Connections (VCC) a Virtual Path Connections (VPC) jsou správně nastaveny s požadovanými parametry Quality of Service (QoS), jako je poměr ztráty buněk a zpoždění. Pro systémy 3GPP tento transportní mechanismus podporoval služby v reálném čase, jako je hlas a video, tím, že poskytoval garantovanou šířku pásma a nízkou latenci, což bylo nezbytné pro nasazení UMTS a raného [HSPA](/mobilnisite/slovnik/hspa/). Tato adresovací schéma také usnadňovalo správu sítě a odstraňování problémů tím, že poskytovalo jasné mapování mezi logickými síťovými prvky a fyzickými rozhraními ATM.

Navzdory své technické robustnosti bylo použití AESA a ATM transportu v pozdějších vydáních 3GPP z velké části nahrazeno IP transportem (s použitím IP adres), počínaje zavedením IP Multimedia Subsystem (IMS) v Rel-5 a plně IP architekturou v Rel-8 (SAE/LTE). AESA však zůstává relevantní v legacy sítích a určitých scénářích backhaul. Jeho specifikace v mnoha dokumentech 3GPP, včetně 21.905 (slovníček), 25.414 (Iu datový transport), 25.424 (Iur datový transport), 25.426 (Iub datový transport) a 29.414 (GTP transport přes ATM), podtrhuje jeho historický význam při zajišťování interoperability a spolehlivého transportu pro raná nasazení sítí 3G a 4G.

## K čemu slouží

AESA byla vytvořena, aby uspokojila potřebu standardizovaného, škálovatelného adresovacího schématu v ATM sítích, které byly dominantní transportní technologií pro telekomunikace na konci 90. let a začátkem 21. století. Před ATM telekomunikační sítě často spoléhaly na okruhově přepínané TDM (Time Division Multiplexing) s point-to-point spojeními, kterým chyběla flexibilita a výhody statistického multiplexování paketově přepínaných sítí. ATM představilo buňkami orientovaný, spojením orientovaný model, který mohl efektivně zpracovávat smíšené typy provozu (hlas, data, video), ale vyžadoval robustní adresovací mechanismus pro identifikaci koncových bodů a vytváření virtuálních okruhů. AESA toto poskytla tím, že nabídla hierarchickou adresní strukturu, která podporovala globální jedinečnost, zjednodušila směrování a integraci s existujícími telefonními číslovacími plány (E.164), čímž vyřešila problém identifikace koncových bodů ve velkých, více-dodavatelských ATM sítích.

Motivace pro přijetí AESA ve standardech 3GPP, počínaje R99, pramenila z požadavku na spolehlivou transportní vrstvu pro novou architekturu UMTS. Rané sítě 3G potřebovaly podporovat jak okruhově přepínané hlasové služby, tak paketově přepínané datové služby s garantovaným QoS. ATM se svým adresováním založeným na AESA nabízelo možnosti traffic engineeringu, explicitní třídy QoS (CBR, VBR, ABR, UBR) a efektivní využití šířky pásma prostřednictvím virtuálních okruhů. To bylo kritické pro rozhraní jako Iu, Iur a Iub, kde nízká latence a minimální jitter byly nezbytné pro komunikaci v rádiové přístupové síti v reálném čase. AESA umožnila těmto rozhraním fungovat přes sdílenou ATM infrastrukturu při zachování izolace a garancí výkonu mezi různými spojeními a síťovými operátory.

Dále AESA řešila omezení předchozích ad-hoc nebo proprietárních adresovacích schémat tím, že poskytovala standardizovaný formát, který zajišťoval interoperabilitu mezi zařízeními od různých výrobců. To bylo zásadní pro globální nasazení sítí 3G, protože umožnilo síťovým operátorům budovat více-dodavatelské sítě bez problémů s kompatibilitou. Použití AESA také usnadňovalo pokročilé síťové funkce, jako je dynamické navazování spojení prostřednictvím SVC, které mohlo být spouštěno na požádání pro efektivní využití zdrojů, a podporu odolnosti sítě přesměrováním v případě selhání. Přestože byla AESA nakonec nahrazena IP pro svou jednoduchost a nižší náklady, sehrála zásadní roli při umožnění vysokovýkonného transportu potřebného pro počáteční úspěch mobilních služeb 3G.

## Klíčové vlastnosti

- Jednoznačná identifikace koncového bodu pro síťové prvky ATM
- Podpora hierarchického adresování založeného na formátech ITU-T E.164 nebo NSAP
- Umožňuje vytváření Permanent Virtual Circuits (PVC) a Switched Virtual Circuits (SVC)
- Nedílná součást signalizačních protokolů jako Q.2931 pro navazování a ukončování spojení
- Usnadňuje poskytování QoS asociací adres s provozními smlouvami
- Poskytuje škálovatelnost pro velké, distribuované telekomunikační sítě

## Související pojmy

- [ATM – Asynchronous Transfer Mode](/mobilnisite/slovnik/atm/)
- [AAL2 – ATM Adaptation Layer type 2](/mobilnisite/slovnik/aal2/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [AESA na 3GPP Explorer](https://3gpp-explorer.com/glossary/aesa/)

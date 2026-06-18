---
slug: "e1ap"
url: "/mobilnisite/slovnik/e1ap/"
type: "slovnik"
title: "E1AP – E1 Application Protocol"
date: 2025-01-01
abbr: "E1AP"
fullName: "E1 Application Protocol"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e1ap/"
summary: "Řídicí protokol fungující přes rozhraní E1 v disagregované 5G rádiové přístupové síti (NG-RAN). Umožňuje komunikaci mezi centrální jednotkou (CU) a distribuovanou jednotkou (DU) a zajišťuje řízení a s"
---

E1AP je řídicí protokol (control plane) fungující přes rozhraní E1 mezi centrální jednotkou (Central Unit, CU) a distribuovanou jednotkou (Distributed Unit, DU) v disagregované 5G rádiové přístupové síti (RAN).

## Popis

E1AP je aplikační protokol definovaný 3GPP pro rozhraní E1, což je klíčové vnitřní rozhraní v rádiové přístupové síti nové generace (NG-RAN) zavedené v 5G systému. Rozhraní E1 spojuje centrální jednotku ([CU](/mobilnisite/slovnik/cu/)) a distribuovanou jednotku ([DU](/mobilnisite/slovnik/du/)) v disagregované stanici gNB (5G základnová stanice) nebo ng-eNB (vylepšená LTE stanice pro 5G core). Toto funkční rozdělení, konkrétně rozdělení CU-DU, je zásadní architektonickou změnou v 5G RAN, která umožňuje oddělení časově kritických funkcí nižších vrstev (DU) od méně časově citlivých funkcí vyšších vrstev (CU). Protokol E1AP funguje nad transportní vrstvou (používá [SCTP](/mobilnisite/slovnik/sctp/)/IP) a je zodpovědný za veškerou signalizaci řídicí roviny mezi těmito dvěma logickými uzly.

Protokol definuje sadu elementárních procedur (Elementary Procedures, EPs), které řídí interakci mezi CU a DU. Tyto procedury jsou kategorizovány jako Třída 1 (vyžadující odpověď) a Třída 2 (nevyžadující odpověď). Mezi klíčové funkce spravované protokolem E1AP patří správa kontextu přenosu (Bearer Context Management – zřízení, změna, uvolnění), aktualizace konfigurace DU a CU, správa mobility pro připojená UE a přenos zpráv [RRC](/mobilnisite/slovnik/rrc/) mezi CU-CP (řídicí část CU) a UE přes DU. Když se UE připojí, CU-CP použije E1AP k vytvoření kontextu přenosu v DU a nakonfiguruje potřebné rádiové prostředky. DU zajišťuje plánování v reálném čase a zpracování fyzické vrstvy, zatímco CU spravuje řízení rádiových prostředků, zabezpečení a připojení k jádru sítě.

Z procedurálního hlediska jsou zprávy E1AP přenášeny v [PDU](/mobilnisite/slovnik/pdu/) (Protocol Data Units) protokolu E1AP. Rozhraní podporuje ukončení referenčních bodů [F1-C](/mobilnisite/slovnik/f1-c/) i [F1-U](/mobilnisite/slovnik/f1-u/) na straně DU, což znamená, že DU komunikuje s CU-CP přes E1 a s CU-UP (uživatelská část CU) přes jiné rozhraní. E1AP je navržen jako budoucně odolný a flexibilní, podporuje různé možnosti funkčního rozdělení (i když Split Option 2, jak je definováno v 3GPP, je pro E1 nejběžnější). Umožňuje centralizovanou koordinaci více DU jedinou CU, což usnadňuje pokročilé funkce, jako je koordinovaný vícebodový přenos (CoMP), vyvažování zátěže a efektivní sdružování prostředků. Toto oddělení je klíčové pro umožnění cloud-nativních nasazení RAN, síťového řezání (network slicing) a flexibilního nezávislého škálování kapacity a pokrytí.

## K čemu slouží

E1AP a rozhraní E1 byly vytvořeny, aby vyřešily potřebu flexibilnější, škálovatelnější a efektivnější architektury RAN pro 5G, což znamená posun od monolitického návrhu základnové stanice z 4G LTE. Tradiční [eNB](/mobilnisite/slovnik/enb/) integrovalo všechny vrstvy rádiového protokolu, což omezovalo flexibilitu nasazení a ztěžovalo centralizaci inteligence pro funkce jako pokročilá koordinace nebo využití prostředků cloud computingu. Účelem rozdělení CU-DU, které E1AP umožňuje, je disagregovat základnovou stanici a umožnit optimální umístění síťových funkcí v síti na základě jejich požadavků na latenci a zpracování.

Tato disagregace řeší několik klíčových problémů. Umožňuje nasazení centralizované RAN (C-RAN), kde může být CU umístěno v regionálním datovém centru a obsluhovat mnoho vzdálených DU. Tato centralizace umožňuje efektivnější sdružování prostředků, snížení prostorových nároků a nákladů na lokalitách s buňkami a zjednodušenou implementaci technik koordinace více buněk. Dále je v souladu s širšími principy návrhu 5G, jako je softwarizace sítě a cloud-nativní design, což umožňuje implementovat CU jako virtualizované síťové funkce (VNFs) nebo cloud-nativní funkce (CNFs) na standardním hardwaru (COTS). E1AP poskytuje standardizovaný řídicí protokol, který toto rozdělení uvádí do provozu a zajišťuje interoperabilitu mezi zařízeními CU a DU od různých výrobců.

Historicky, před standardizací 3GPP, byly v některých před-5G implementacích C-RAN používány proprietární rozdělení a rozhraní, což vedlo k závislosti na dodavateli. Standardizace E1AP ve verzi 15 (Release 15) byla motivována snahou průmyslu o interoperabilitu mezi více dodavateli a jasné, otevřené rozhraní. Umožňuje operátorům kombinovat CU od jednoho dodavatele s DU od jiného, což podporuje konkurenci a inovace. Rozhraní E1 s E1AP jako jeho mozkem je tedy základním kamenem hnutí Open RAN (O-RAN) a je nezbytné pro dosažení plných ekonomických a výkonnostních benefitů virtualizované, disagregované 5G RAN.

## Klíčové vlastnosti

- Definuje signalizaci řídicí roviny pro rozhraní E1 mezi CU a DU v 5G NG-RAN
- Spravuje zřízení, změnu a uvolnění kontextu přenosu (Bearer Context) pro uživatelské zařízení (UE)
- Podporuje přenos zpráv RRC mezi CU-CP a UE přes DU
- Umožňuje výměnu konfigurace a informací o podporovaných funkcích mezi CU a DU
- Usnadňuje procedury správy mobility pro UE v připojeném stavu (connected mode)
- Navržen pro podporu různých možností funkčního rozdělení a interoperability mezi více dodavateli

## Související pojmy

- [F1AP – F1 Application Protocol](/mobilnisite/slovnik/f1ap/)

## Definující specifikace

- **TS 37.480** (Rel-19) — E1 Interface General Aspects and Principles
- **TS 38.460** (Rel-19) — E1 Interface General Aspects and Principles

---

📖 **Anglický originál a plná specifikace:** [E1AP na 3GPP Explorer](https://3gpp-explorer.com/glossary/e1ap/)

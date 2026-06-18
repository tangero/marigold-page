---
slug: "cas"
url: "/mobilnisite/slovnik/cas/"
type: "slovnik"
title: "CAS – Channel Associated Signalling"
date: 2026-01-01
abbr: "CAS"
fullName: "Channel Associated Signalling"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cas/"
summary: "Channel Associated Signalling (CAS, signalizace přidružená ke kanálu) je zastaralá signalizační metoda v telefonii, při níž řídicí informace putují stejným fyzickým kanálem jako hlasový/datový provoz."
---

CAS je zastaralá signalizační metoda v telefonii, při níž řídicí informace putují stejným fyzickým kanálem jako hlasový nebo datový provoz.

## Popis

Channel Associated Signalling (CAS, signalizace přidružená ke kanálu) je signalizační architektura v telekomunikacích, při níž se signalizační informace potřebné pro zřízení, dohled a ukončení hovoru přenášejí ve stejném fyzickém přenosovém kanálu (nebo v kanálu k němu trvale přidruženém) jako uživatelský hlasový nebo datový provoz. V digitálních přenosových systémech T1/E1 se to typicky implementuje 'kradením' konkrétních bitů z uživatelského datového toku v rámci každého rámce pro přenos signalizačního stavu. Například v systému T1 s 24 kanály a formátem [PCM](/mobilnisite/slovnik/pcm/) používajícím Super Frame ([SF](/mobilnisite/slovnik/sf/)) se nejméně významný bit (8. bit) 6. a 12. rámce každého superrámce o 12 rámcích používá pro signalizaci každého kanálu. Ve formátu Extended Super Frame (ESF) se bity kradou z 6., 12., 18. a 24. rámce.

Fungování CAS je neodmyslitelně svázáno s časovou strukturou fyzického přenosového média. Každý hlasový kanál (např. 64 kbps DS0 timeslot) má svou vlastní vyhrazenou signalizační cestu v pásmu. Signalizační informace je jednoduchá a typicky představuje malou množinu stavů, jako je volno, zvednuto, položeno, vyzvánění a 'wink'. Tyto informace se přenášejí opakovaně, což přijímacímu zařízení umožňuje neustále sledovat stav linky. Protože je signalizace fyzicky svázána se svým provozním kanálem, zřízení hovoru znamená vyhrazení jak přenosové cesty, tak její přidružené signalizační kapacity po dobu trvání spojení.

Klíčovými komponentami v síti založené na CAS jsou channel banky nebo multiplexory, které provádějí analogově-digitální převod a vkládají/extrahují signalizaci kradením bitů, a digitální ústředny vybavené CAS trunkovými kartami pro interpretaci těchto signálů. Protokol je jednoduchý a deterministický, s nízkou režií pro jeden kanál, ale postrádá flexibilitu, rychlost a bohatou funkcionalitu signalizace společným kanálem. Jeho fungování je transparentní vůči uživatelským datům, ačkoliv technika kradení bitů během signalizačních rámců teoreticky snižuje věrnost hlasového kanálu z 8bitového na 7,5bitové kódování µ-law/A-law.

V kontextu specifikací 3GPP je CAS primárně zmiňována v souvislosti s legacy scénáři pro spolupráci a migraci. Zatímco systémy 3GPP od GSM výše převážně používají pro funkce jádra sítě signalizaci společným kanálem (např. [SS7](/mobilnisite/slovnik/ss7/), SIGTRAN, Diameter), CAS rozhraní mohou být relevantní tam, kde se mobilní síť propojuje s tradiční [PSTN](/mobilnisite/slovnik/pstn/) nebo legacy [PBX](/mobilnisite/slovnik/pbx/) systémy. Specifikace jako TS 29.424 a TS 29.558 mohou odkazovat na CAS v kontextu signalizačních funkcí pro spolupráci ([IWF](/mobilnisite/slovnik/iwf/)), které překládají mezi [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo jinými protokoly a legacy CAS signalizací za účelem usnadnění koncové řízení hovorů v hybridních sítích.

## K čemu slouží

CAS byla vyvinuta jako základní metoda signalizace v raných digitálních telefonních sítích, nejvýznamněji u přenosových systémů T1 (1,544 Mbps) a E1 (2,048 Mbps) zavedených v 60. a 70. letech 20. století. Jejím primárním účelem bylo poskytnout přímočarý mechanismus signalizace pro jednotlivé kanály pro dohledovou signalizaci (obsazení, odpověď, rozpojení) a adresovou signalizaci (volané číslice) bez nutnosti samostatné, složité signalizační sítě. Řešila problém efektivní integrace řídicích funkcí do rodící se digitální přenosové infrastruktury a nahradila tak samostatné smyčky stejnosměrné signalizace nebo jednofrekvenční tóny používané v analogových přenosových systémech.

Motivací pro CAS byla jednoduchost, přímá asociace a nákladová efektivita pro point-to-point trunková spojení. Protože každý hlasový kanál nesl své vlastní řídicí bity, nebyla potřeba sofistikovaná signalizační síť s přepojováním paketů ani složité protokolové zásobníky vysoké úrovně. To usnadnilo návrh a nasazení raných digitálních ústředen a channel bank. Byla dokonale vhodná pro éru telefonie s přepojováním okruhů, kdy se zřizovalo a udržovalo fyzické koncové spojení a přidružená signalizace se mohla snadno 'ukrást' z již synchronizovaného digitálního bitového toku.

CAS má však významná omezení, která motivovala celoprůmyslový přechod k signalizaci společným kanálem (CCS). Její povaha v pásmu ji činí náchylnou k podvodům (např. 'blue boxing'), kdy lze tóny napodobit signalizaci. Je neefektivní pro služby s bohatou funkcionalitou, protože signalizační šířka pásma je minimální a nemůže snadno přenášet dodatečné informace. Zřizování hovoru je pomalejší, protože signalizaci lze odesílat pouze během konkrétních rámců s ukradenými bity. Nejzásadnější je, že signalizační cesta je dostupná pouze tehdy, když je zřízen provozní kanál, což brání funkcím jako volání na obsazenou linku. Přijetí architektur založených na CCS v 3GPP od samého počátku byla přímou reakcí na tato omezení a umožnila rychlejší, bezpečnější a inteligentnější síťové služby.

## Klíčové vlastnosti

- Signalizace v pásmu přenášená ve stejném přenosovém kanálu jako uživatelský provoz
- Používá signalizaci 'kradením bitů' v rámcích T1/E1, obětuje integritu uživatelských bitů pro řízení
- Jednoduchá stavová signalizace (položeno, zvednuto, vyzvánění, wink)
- Přímá fyzická asociace mezi jednou signalizační cestou a jedním přenosovým kanálem
- Deterministické časování svázané se strukturou PCM rámců (např. každý 6. rámec)
- Primárně používána pro dohledovou a adresovou signalizaci v spojích s přepojováním okruhů

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [PCM – Pulse Code Modulation](/mobilnisite/slovnik/pcm/)

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 36.976** (Rel-19) — LTE-based 5G Terrestrial Broadcast Overview

---

📖 **Anglický originál a plná specifikace:** [CAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cas/)

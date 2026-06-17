---
slug: "ble"
url: "/mobilnisite/slovnik/ble/"
type: "slovnik"
title: "BLE – Bluetooth Low Energy"
date: 2025-01-01
abbr: "BLE"
fullName: "Bluetooth Low Energy"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ble/"
summary: "BLE je nízkopříkonová bezdrátová komunikační technologie standardizovaná 3GPP pro připojení zařízení IoT. Umožňuje energeticky efektivní výměnu dat mezi zařízeními na krátké vzdálenosti a podporuje ap"
---

BLE je nízkopříkonová bezdrátová technologie standardizovaná 3GPP pro připojení IoT, která umožňuje energeticky efektivní výměnu dat na krátké vzdálenosti za účelem podpory konvergence buněčných sítí a IoT a služeb založených na blízkosti.

## Popis

Bluetooth Low Energy (BLE) je technologie bezdrátové osobní sítě navržená pro nízkopříkonovou komunikaci na krátkou vzdálenost. V rámci norem 3GPP je BLE integrována jako doplňková technologie k buněčným sítím, zejména pro internet věcí (IoT) a služby založené na blízkosti. Technologie pracuje v pásmu 2,4 GHz [ISM](/mobilnisite/slovnik/ism/) a používá rozprostřené spektrum s přeskakováním kmitočtu na 40 kanálech (37 datových kanálů a 3 reklamní kanály). Protokolová architektura BLE se skládá z vrstev Controller (PHY a Link Layer) a Host (Logical Link Control and Adaptation Protocol, Security Manager, Attribute Protocol a Generic Attribute Profile), což umožňuje efektivní výměnu dat s minimální spotřebou energie.

BLE pracuje v režimech s navázáním spojení a bez spojení. V režimu bez spojení zařízení vysílají reklamní pakety na třech primárních reklamních kanálech, což umožňuje jiným zařízením je objevit bez nutnosti navázat trvalé spojení. Jakmile je spojení navázáno, zařízení komunikují na 37 datových kanálech pomocí adaptivního přeskakování kmitočtu ke zmírnění rušení. Parametry spojení, včetně intervalu spojení, latence podřízeného zařízení a časového limitu dohledu, jsou mezi zařízeními vyjednány tak, aby optimalizovaly spotřebu energie podle požadavků aplikace. BLE podporuje přenosové rychlosti až 2 Mbps (s [LE](/mobilnisite/slovnik/le/) 2M PHY) při zachování ultranízké spotřeby energie díky optimalizovanému střídání činnosti a režimům spánku.

V architekturách 3GPP integrace BLE umožňuje několik klíčových funkcionalit. Pro služby založené na blízkosti (ProSe) lze BLE použít pro zjišťování a komunikaci mezi zařízeními ve spojení se sítěmi LTE/5G. Pro aplikace IoT slouží BLE jako technologie lokální konektivity, která může spolupracovat s buněčnými modemy pro širokopásmový přenos. Generic Attribute Profile (GATT) definuje hierarchickou datovou strukturu využívající charakteristiky a služby, což umožňuje standardizovanou výměnu dat mezi zařízeními BLE. Bezpečnostní funkce zahrnují párování, vytváření vazeb a šifrování pomocí AES-CCM s podporou jak starších metod párování, tak LE Secure Connections.

Specifikace 3GPP definují body integrace BLE s buněčnými sítěmi, včetně mechanismů pro BLE asistované určování polohy, spouštění zařízení IoT pro buněčné sítě založené na BLE a vzájemné spolupráce BLE-WLAN-buněčných sítí. Nízká spotřeba energie technologie (umožňující výdrž baterií v řádu měsíců až let), minimální implementační složitost a rozšířený ekosystém z ní činí cennou součást komplexního rámce konektivity 3GPP pro různé scénáře IoT a služeb založených na blízkosti.

## K čemu slouží

BLE bylo vytvořeno pro uspokojení potřeby ultranízkopříkonové bezdrátové konektivity pro zařízení s omezenými energetickými zdroji. Klasický Bluetooth (Bluetooth Classic) spotřebovával příliš mnoho energie pro aplikace jako senzory, nositelná elektronika a majáčky, které vyžadují měsíce či roky výdrže z článkových baterií. BLE tento problém řeší optimalizací protokolu pro minimální dobu činnosti a efektivní režimy spánku při zachování spolehlivé komunikace na krátkou vzdálenost.

V rámci norem 3GPP integrace BLE řeší rostoucí potřebu heterogenní síťové konektivity, kde buněčné sítě poskytují širokoplošné pokrytí, zatímco technologie krátkého dosahu, jako je BLE, efektivně zvládají lokální konektivitu. To je zvláště důležité pro aplikace IoT, kde zařízení mohou potřebovat komunikovat s lokálními bránami nebo jinými blízkými zařízeními při šetření energií baterie. BLE umožňuje nákladově efektivní nasazení masivního množství zařízení IoT snížením využití buněčného rádiového rozhraní pro místní komunikaci.

Technologie také podporuje služby založené na blízkosti, které doplňují schopnosti buněčných sítí, jako je zjišťování zařízení, místní výměna dat a služby založené na poloze. Standardizací integrace BLE ve specifikacích 3GPP průmysl zajišťuje interoperabilitu mezi ekosystémy buněčných sítí a BLE, což umožňuje bezproblémové uživatelské zážitky napříč různými doménami konektivity při optimalizaci spotřeby energie a využití síťových zdrojů.

## Klíčové vlastnosti

- Ultranízká spotřeba energie umožňující roky výdrže baterií
- Podpora režimů komunikace s navázáním spojení i bez spojení
- Adaptivní přeskakování kmitočtu na 40 kanálech v pásmu 2,4 GHz
- Přenosové rychlosti až 2 Mbps s LE 2M PHY
- Komplexní zabezpečení se šifrováním AES-CCM a více metodami párování
- Generic Attribute Profile (GATT) pro standardizované vyhledávání služeb a výměnu dat

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 37.571** (Rel-19) — UE Conformance for Positioning

---

📖 **Anglický originál a plná specifikace:** [BLE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ble/)

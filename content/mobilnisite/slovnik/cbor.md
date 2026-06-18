---
slug: "cbor"
url: "/mobilnisite/slovnik/cbor/"
type: "slovnik"
title: "CBOR – Concise Binary Object Representation"
date: 2025-01-01
abbr: "CBOR"
fullName: "Concise Binary Object Representation"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cbor/"
summary: "CBOR je kompaktní binární formát dat navržený pro prostředí s omezenými zdroji, jako jsou zařízení IoT. Poskytuje efektivní kódování strukturovaných dat s minimální režií, což umožňuje efektivní komun"
---

CBOR je kompaktní binární formát dat navržený pro prostředí s omezenými zdroji, jako jsou zařízení IoT, který umožňuje efektivní komunikaci v sítích 5G díky snížení požadavků na šířku pásma a výpočetní výkon.

## Popis

Concise Binary Object Representation (CBOR) je binární formát pro serializaci dat specifikovaný v [RFC](/mobilnisite/slovnik/rfc/) 7049, který byl přijat organizací 3GPP pro různé aplikace, zejména v prostředí IoT a zařízení s omezenými zdroji. Na rozdíl od textových formátů, jako je [JSON](/mobilnisite/slovnik/json/), CBOR používá kompaktní binární kódování, které výrazně snižuje velikost zpráv při zachování sémantiky čitelné pro člověka. Formát je samopopisný prostřednictvím jednoduché struktury typ-délka-hodnota, kde každá datová položka obsahuje informaci o typu, volitelnou délku a vlastní hodnotu. Tento návrh umožňuje efektivní parsování bez nutnosti definic schémat a zároveň zachovává rozšiřitelnost pomocí mechanismu značek (tagů).

Architektura CBOR používá přímočaré schéma kódování, kde první bajt (hlavní typ) označuje datový typ (celé číslo, bajtový řetězec, textový řetězec, pole, mapa, značka nebo jednoduchá hodnota) a dodatečné informace. Hlavní typ zabírá tři nejvýznamnější bity, zatímco pět nejméně významných bitů obsahuje dodatečné informace nebo malou celočíselnou hodnotu. Pro větší hodnoty dodatečné informace udávají, zda následující bajty obsahují skutečnou délku nebo hodnotu. Toto kódování s proměnnou délkou zajišťuje kompaktní reprezentaci pro malé hodnoty a zároveň podporuje libovolně velké datové struktury, když je to potřeba.

V systémech 3GPP slouží CBOR jako podkladový kódovací formát pro různé protokoly a rozhraní, zejména ta zahrnující zařízení s omezenými zdroji. Používá se v protokolu Lightweight M2M (LwM2M) pro správu zařízení, v bezpečnostních protokolech pro kódování certifikátů a v protokolech servisní vrstvy pro efektivní výměnu dat. Deterministická pravidla kódování formátu zajišťují, že identické datové struktury vytvoří identické sekvence bajtů, což je klíčové pro kryptografické operace, jako jsou digitální podpisy a kódy pro ověření zpráv.

Klíčové součásti CBOR zahrnují systém značek, který umožňuje sémantické anotování datových položek, kódování s neurčitou délkou pro streamové aplikace a jednoduché hodnoty, které zahrnují standardní logické hodnoty, hodnotu null a nedefinovanou hodnotu spolu s rezervovaným prostorem pro budoucí rozšíření. Formát podporuje čísla s plovoucí řádovou čárkou v poloviční (16bitové), jednoduché (32bitové) a dvojnásobné (64bitové) přesnosti, což jej činí vhodným pro vědecké a měřicí aplikace. Návrh CBOR klade důraz jak na kompaktnost, tak na efektivitu zpracování, přičemž parsery typicky vyžadují minimální paměť a výpočetní výkon ve srovnání s textovými alternativami.

V sítích 5G hraje CBOR klíčovou roli při umožnění efektivní komunikace pro masivní nasazení IoT, kde zařízení mají výrazná omezení v oblasti napájení, paměti a výpočetního výkonu. Je integrován do různých specifikací 3GPP pro protokoly servisní vrstvy, správu bezpečnostních přihlašovacích údajů a rozhraní pro správu zařízení. Rozšiřitelnost formátu prostřednictvím značek umožňuje 3GPP definovat datové typy specifické pro danou doménu při zachování interoperability s obecnými implementacemi CBOR.

## K čemu slouží

CBOR byl vytvořen, aby řešil omezení textových datových formátů, jako jsou [JSON](/mobilnisite/slovnik/json/) a [XML](/mobilnisite/slovnik/xml/), v prostředích s omezenými zdroji, typických pro IoT a mobilní aplikace. Tyto textové formáty, ačkoli jsou čitelné pro člověka a široce podporované, způsobují značnou režii z hlediska spotřeby šířky pásma a výpočetních požadavků. Pro napájením z baterie závislá IoT zařízení s omezenými výpočetními zdroji pracující přes připojení s nízkou šířkou pásma se tato režie stává nepřekonatelnou překážkou. CBOR poskytuje efektivnější alternativu, která zachovává strukturální flexibilitu JSON, ale dramaticky snižuje velikost kódování a složitost parsování.

Historický kontext přijetí CBOR v 3GPP vychází z exponenciálního růstu zařízení IoT a potřeby efektivní komunikace mezi stroji v sítích 5G. Předchozí přístupy používající XML nebo JSON vyžadovaly značný výpočetní výkon a paměť pro parsování a generování, což bylo v rozporu s omezenými zdroji mnoha IoT zařízení. Navíc podrobná povaha textových formátů spotřebovávala nadměrnou šířku pásma, což snižovalo výdrž baterie a zvyšovalo provozní náklady pro nasazení celulárního IoT.

CBOR tyto problémy řeší prostřednictvím svého kompaktního binárního kódování, které odstraňuje potřebu názvů polí v každé zprávě, používá efektivní numerické reprezentace a minimalizuje strukturální režii. Návrh formátu konkrétně zohledňuje potřeby zařízení s omezenými zdroji, s parsovacími algoritmy, které mohou pracovat s minimální pamětí a předvídatelnou dobou zpracování. To činí CBOR zvláště vhodným pro případy použití masivní komunikace mezi stroji (mMTC) v 3GPP, kde tisíce zařízení potřebují efektivně komunikovat se síťovými servery.

## Klíčové vlastnosti

- Kompaktní binární kódování s výrazně menší velikostí zpráv než u textových formátů
- Samopopisný datový formát, který pro základní parsování nevyžaduje externí schéma
- Deterministické kódování zajišťující, že identická data vytvoří identické sekvence bajtů
- Rozšiřitelný systém značek pro sémantickou anotaci datových položek
- Podpora streamování prostřednictvím polí a map s neurčitou délkou
- Efektivní parsovací algoritmy vhodné pro zařízení s omezenými zdroji a malou pamětí

## Související pojmy

- [JSON – JavaScript Object Notation](/mobilnisite/slovnik/json/)

## Definující specifikace

- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- **TS 33.220** (Rel-19) — Generic Authentication Architecture (GAA); Generic Bootstrapping Architecture (GBA)
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [CBOR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbor/)

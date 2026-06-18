---
slug: "h-ees"
url: "/mobilnisite/slovnik/h-ees/"
type: "slovnik"
title: "H-EES – Home Edge Enabler Server"
date: 2026-01-01
abbr: "H-EES"
fullName: "Home Edge Enabler Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/h-ees/"
summary: "Home Edge Enabler Server (H-EES) je síťová funkce zavedená ve specifikaci 3GPP Release 18 pro správu a orchestraci aplikací a služeb edge computingu pro roamující uživatele. Nachází se v domovské veře"
---

H-EES je síťová funkce v domovské síti uživatele, která spravuje služby edge computingu pro roamující uživatele koordinací se serverem navštívené sítě, aby zajistila konzistentní poskytování služeb s nízkou latencí.

## Popis

Home Edge Enabler Server (H-EES) je klíčová komponenta architektury 3GPP Edge Computing definované v TS 23.558. Funguje v rámci domovské veřejné pozemní mobilní sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)) účastníka a slouží jako centrální řídicí bod pro zpřístupnění edge aplikací, když uživatel roamuje. H-EES nehostí samotné edge aplikace; místo toho spravuje aspekty registrace služeb, jejich vyhledávání a kontinuity relací. Udržuje registr dostupných edge aplikací a služeb, k nimž je uživatel přihlášen nebo které nabízí domovský operátor. Když roamující uživatel požádá o edge službu, H-EES komunikuje s Visited Edge Enabler Server ([V-EES](/mobilnisite/slovnik/v-ees/)) v navštívené veřejné pozemní mobilní síti ([VPLMN](/mobilnisite/slovnik/vplmn/)), aby usnadnil její zřízení. Tato interakce zahrnuje autorizaci žádosti o službu, vyhledání vhodných instancí edge aplikací v navštívené síti na základě požadavků na latenci a polohy uživatele a zajištění uplatnění uživatelského profilu a politik služeb. H-EES komunikuje s V-EES přes referenční bod Ees-EE (Edge Enabler Server - Edge Enabler). Jeho architektura je navržena odděleně od uživatelské roviny a zaměřuje se na řídicí a správní funkce. Integruje se s Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) pro zabezpečené vystavení [API](/mobilnisite/slovnik/api/) a s Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro data účastníků. H-EES hraje klíčovou roli v ekosystému edge computingu tím, že abstrahuje složitost podkladové síťové topologie od poskytovatelů aplikací a umožňuje jim nabízet uživatelům bezproblémové služby s nízkou latencí napříč různými doménami operátorů.

## K čemu slouží

H-EES byl vytvořen, aby vyřešil výzvu poskytování konzistentních služeb edge computingu s nízkou latencí mobilním uživatelům, kteří roamují mimo svou domovskou síť. Před jeho zavedením byla nasazení edge computingu z velké části omezena na domény jednotlivých operátorů, což ztěžovalo garantování výkonnostních požadavků aplikací, jako jsou autonomní vozidla, rozšířená realita nebo hry v reálném čase, pro cestující účastníky. Nedostatek standardizovaného mechanismu pro kontrolu domovské sítě a vynucování politik v edge prostředí navštívené sítě bránil komerčnímu rozšíření globálních edge služeb. H-EES to řeší tím, že poskytuje standardizovanou kotvu domovské sítě pro správu edge služeb. Umožňuje domovskému operátorovi udržovat kontrolu nad uživatelským zážitkem ze služby, uplatňovat konzistentní politiky a zajišťovat bezpečnost a integritu účtování, i když jsou výpočetní prostředky v cizí síti. Jeho vytvoření v Release 18 bylo motivováno snahou odvětví o všudypřítomný edge computing a potřebou 3GPP definovat roamingovou architekturu pro sítě 5G Advanced, což usnadňuje interoperabilitu mezi operátory a podporuje širší ekosystém pro vývojáře edge aplikací.

## Klíčové vlastnosti

- Centralizovaný registr služeb a vyhledávání pro edge aplikace v HPLMN
- Orchestrace relací edge služeb pro roamující uživatele ve spolupráci s V-EES
- Zpracování a autorizace žádostí Application Function (AF) pro edge služby
- Podpora mobility edge aplikací a kontinuity služeb během pohybu uživatele
- Integrace s NEF pro zabezpečené vystavení aplikací třetích stran
- Vynucování politik pro přístup k edge službám na základě profilů domovského účastníka

## Související pojmy

- [V-EES – Visited Edge Enabler Server](/mobilnisite/slovnik/v-ees/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications

---

📖 **Anglický originál a plná specifikace:** [H-EES na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-ees/)

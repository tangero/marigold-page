---
slug: "fnr"
url: "/mobilnisite/slovnik/fnr/"
type: "slovnik"
title: "FNR – Flexible Number Register"
date: 2025-01-01
abbr: "FNR"
fullName: "Flexible Number Register"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/fnr/"
summary: "Flexible Number Register (FNR) je koncept správy 3GPP pro centralizovanou databázi, která ukládá a spravuje nedialovatelná čísla a identifikátory používané v rámci síťových operací a managementu. Posk"
---

FNR je centralizovaná databáze 3GPP pro ukládání a správu nedialovatelných síťových identifikátorů, jako jsou sériová čísla zařízení a verze softwaru, která umožňuje sledování aktiv a správu konfigurace.

## Popis

Flexible Number Register (FNR) je v rámci frameworku Telecom Management 3GPP definován jako logická funkce odpovědná za ukládání, přidělování a správu různých nedialovatelných čísel a identifikátorů používaných v síti. Na rozdíl od databází účastníků, jako je [HSS](/mobilnisite/slovnik/hss/), se FNR zabývá identifikátory souvisejícími se samotnou síťovou infrastrukturou. Funguje jako centralizovaný, autoritativní zdroj dat, která jsou klíčová pro zřizování sítě, správu inventáře, správu poruch a reportování výkonu. Architektura FNR je typicky databázová nebo představuje sadu integrovaných datových úložišť přístupných prostřednictvím standardizovaných rozhraní pro správu, jako jsou například ta založená na [FNIM](/mobilnisite/slovnik/fnim/).

Fungování FNR zahrnuje několik klíčových procesů. Za prvé poskytuje registrační službu, kde si síťové elementy nebo systémy pro správu mohou registrovat identifikátory při nasazení nového zařízení nebo vytvoření nových logických prostředků. Například při instalaci nové základnové stanice (gNB) může být její jedinečný globální identifikátor, výrobní sériové číslo a nainstalované verze hardwaru/softwaru zaregistrovány v FNR. Za druhé podporuje funkce dotazování a vyhledávání, což umožňuje jiným Operations Support Systems ([OSS](/mobilnisite/slovnik/oss/)) informace vyhledávat. Systém správy poruch může například dotazem na FNR získat přesnou polohu a technický kontakt pro selhávající zařízení na základě jeho identifikátoru z alarmu. Za třetí FNR spravuje životní cyklus těchto identifikátorů, aktualizuje záznamy během údržby (např. po upgradu softwaru) a označuje je jako vyřazené při likvidaci zařízení.

Klíčové součásti konceptu FNR zahrnují datový model (definující, jaké typy identifikátorů se ukládají, například Equipment Serial Numbers, Location Area Codes nebo Tracking Area Codes), rozhraní pro správu (např. pro northbound integraci s [NMS](/mobilnisite/slovnik/nms/)) a alokační politiky pro určité rozsahy identifikátorů. Jeho úlohou v síti je snížit provozní složitost a chyby odstraněním roztříštěných, nekonzistentních tabulek nebo proprietárních databází zařízení. Tím, že existuje jediný 'zdroj pravdy' pro identifikátory síťových aktiv, mohou operátoři automatizovat procesy jako aktivace služeb, zjednodušit audit a reportování pro compliance a výrazně zlepšit přesnost svého síťového inventáře – což je klíčová schopnost pro velké a vyvíjející se sítě.

## K čemu slouží

FNR byl vytvořen, aby vyřešil provozní neefektivitu a problémy s integritou dat způsobené decentralizovanou, ad-hoc správou identifikátorů síťové infrastruktury. V raných mobilních sítích byly identifikátory pro zařízení, lokality a verze softwaru často spravovány lokálně různými odděleními pomocí odlišných nástrojů nebo dokonce manuálních záznamů. To vedlo k nekonzistentnostem, obtížím při korelaci dat napříč systémy (např. při propojení alarmu ze síťového elementu s jeho fyzickou polohou a servisní smlouvou) a k chybám během rozšiřování nebo rekonfigurace sítě.

Hlavní motivací byla podpora automatizovaného síťového managementu a Self-Organizing Networks (SON). Funkce SON, jako je automatická správa sousedních vztahů ([ANR](/mobilnisite/slovnik/anr/)) nebo autokonfigurace nových základnových stanic, vyžadují spolehlivá a dostupná data o síťových elementech. FNR toto poskytuje tím, že slouží jako centralizované úložiště, které mohou funkce SON a další [OSS](/mobilnisite/slovnik/oss/)/[BSS](/mobilnisite/slovnik/bss/) aplikace dotazovat. Řeší tak omezení předchozích přístupů standardizací typů spravovaných identifikátorů a návrhem jednotné architektonické funkce pro jejich správu.

Představený v Release 8 spolu s ranými nasazeními LTE, získal koncept FNR na významu s růstem a zvyšující se složitostí sítí. Poskytuje základní datovou vrstvu pro přesný síťový inventář, který je nezbytný pro kontrolu nákladů, plánování a efektivní provoz. Dále, v kontextu virtualizace sítí a cloud-nativního 5G, kde mohou být síťové funkce dynamicky instanciovány a škálovány, se role FNR rozšiřuje na správu identifikátorů pro virtuální prostředky, čímž zajišťuje, že i ve vysoce fluidním softwarovém prostředí může být každá komponenta jednoznačně identifikována a sledována pro účely managementu.

## Klíčové vlastnosti

- Centralizované ukládání a správa nedialovatelných identifikátorů síťového zařízení a prostředků
- Podpora životního cyklu záznamů identifikátorů: registrace, dotazování, aktualizace a vyřazení
- Poskytuje standardizovaný datový model pro typy identifikátorů relevantní pro správu sítě
- Umožňuje integraci se systémy pro správu poruch, konfigurace, účtování, výkonu a bezpečnosti (FCAPS)
- Usnadňuje automatizované zřizování sítě a funkce Self-Organizing Network (SON)
- Zvyšuje přesnost síťového inventáře a sledování aktiv pro provozní a obchodní podporu

## Související pojmy

- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service

---

📖 **Anglický originál a plná specifikace:** [FNR na 3GPP Explorer](https://3gpp-explorer.com/glossary/fnr/)

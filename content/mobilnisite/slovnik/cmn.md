---
slug: "cmn"
url: "/mobilnisite/slovnik/cmn/"
type: "slovnik"
title: "CMN – CAMEL Modified Number"
date: 2025-01-01
abbr: "CMN"
fullName: "CAMEL Modified Number"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cmn/"
summary: "Služba CAMEL (Customised Applications for Mobile networks Enhanced Logic), která během sestavování hovoru modifikuje číslo cíle volání. Umožňuje inteligentní překlad čísel založený na síti inteligentn"
---

CMN je služba CAMEL, která během sestavování hovoru modifikuje číslo cíle volání, aby umožnila inteligentní překlad čísel založený na síti inteligentních služeb (IN) pro služby jako přenos čísel (number portability) a směrování ve VPN.

## Popis

[CAMEL](/mobilnisite/slovnik/camel/) Modified Number (CMN) je služba CAMEL fungující v rámci architektury sítě inteligentních služeb (Intelligent Network – [IN](/mobilnisite/slovnik/in/)) v sítích GSM/UMTS. Když účastník zahájí hovor, prostředí CAMEL služeb (CAMEL Service Environment – [CSE](/mobilnisite/slovnik/cse/)) zachytí požadavek na sestavení hovoru a aplikuje logiku pro modifikaci čísla cíle na základě předdefinované servisní logiky. Tato modifikace nastane předtím, než je hovor směrován sítí, což umožňuje dynamický překlad čísel bez nutnosti změn na účastnickém terminálu nebo v jádrové přepínací infrastruktuře.

Služba funguje prostřednictvím interakce mezi mobilní ústřednou (Mobile Switching Center – [MSC](/mobilnisite/slovnik/msc/)) a řídicím bodem služeb (Service Control Point – [SCP](/mobilnisite/slovnik/scp/)) za použití protokolu CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)). Když účastník s aktivní službou CMN zahájí hovor, MSC detekuje CAMEL spouštěč (trigger) a odešle zprávu InitialDP do SCP. SCP následně vykoná servisní logiku, která na základě faktorů jako denní doba, identita volajícího nebo typ služby určí příslušné modifikované cílové číslo. SCP vrátí MSC zprávu Connect s modifikovaným cílovým číslem, které MSC následně použije pro směrování hovoru.

Klíčové komponenty zahrnují prostředí CAMEL služeb (CSE) obsahující servisní logiku, řídicí bod služeb (SCP), který tuto logiku vykonává, a mobilní ústřednu (MSC), která provádí modifikaci čísla. Služba se opírá o informace o CAMEL předplatném uložené v domovském registračním uzlu (Home Location Register – [HLR](/mobilnisite/slovnik/hlr/)), které indikují, kteří účastníci mají schopnost CMN. MSC tyto informace využívá k aktivaci CAMEL interakcí, když tito účastníci volají.

CMN hraje klíčovou roli při umožnění pokročilých telefonních služeb bez nutnosti změn infrastruktury v celé síti. Centralizací logiky pro modifikaci čísel v SCP mohou operátoři služby rychle nasazovat a centrálně spravovat. Služba podporuje různé obchodní aplikace včetně virtuálních privátních sítí, inteligentního směrování na základě času nebo polohy a integraci s externími databázemi pro služby jako přenos čísel.

## K čemu slouží

CMN byl vytvořen k řešení potřeby inteligentního směrování hovorů a služeb překladu čísel v mobilních sítích bez nutnosti změn na účastnických terminálech nebo v jádrových přepínačích. Před službami [CAMEL](/mobilnisite/slovnik/camel/) vyžadovala modifikace čísel buď předprogramované terminály, nebo složité konfigurace ústředen, které bylo obtížné spravovat a škálovat. Mezi omezení těchto přístupů patřil nedostatek flexibility, vysoké náklady na údržbu a neschopnost implementovat centralizovanou servisní logiku.

Historickým kontextem vývoje CMN byla rostoucí poptávka po službách sítě inteligentních služeb (IN) v sítích GSM na konci 90. let 20. století. Když mobilní operátoři rozšiřovali své služby mimo základní hlasové hovory, potřebovali mechanismy pro implementaci služeb jako bezplatná čísla, služby s prémiovým tarifem a virtuální privátní sítě. Tradiční řešení založená na ústřednách byla závislá na dodavateli a obtížně integrovatelná napříč sítěmi více dodavatelů. CAMEL poskytlo standardizovaný přístup k službám sítě IN, přičemž CMN konkrétně řešilo potřebu dynamické modifikace čísel.

CMN řeší problém implementace služeb založených na číslech standardizovaným a škálovatelným způsobem. Umožňuje operátorům nabízet služby jako přenos čísel (kde musí být hovory na přenesená čísla přesměrovány na nová síťová určení), služby VPN (kde se krátké kódy překládají na plná telefonní čísla) a inteligentní směrování na základě obchodních pravidel. Centralizací logiky v SCP mohou operátoři služby rychle nasazovat a upravovat bez nutnosti upgrade ústředen nebo změn konfigurace napříč více síťovými elementy.

## Klíčové vlastnosti

- Dynamický překlad čísel během sestavování hovoru
- Integrace s prostředím CAMEL služeb (CSE) pro centralizovanou logiku
- Podpora pravidel směrování založených na čase a podmínkách
- Kompatibilita s existující infrastrukturou MSC/HLR
- Standardizované rozhraní protokolu CAP mezi MSC a SCP
- Aktivace na základě předplatného prostřednictvím profilu v HLR

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [CMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmn/)

---
slug: "ccd"
url: "/mobilnisite/slovnik/ccd/"
type: "slovnik"
title: "CCD – Conference Call Device"
date: 2025-01-01
abbr: "CCD"
fullName: "Conference Call Device"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ccd/"
summary: "Conference Call Device (CCD) je funkční entita definovaná v 3GPP pro správu víceúčastnických konferenčních hovorů v rámci IP Multimedia Subsystem (IMS). Poskytuje řídicí logiku a schopnosti zpracování"
---

CCD je funkční entita v IP Multimedia Subsystem (IMS), která spravuje řídicí logiku a zpracování médií pro zřizování, udržování a ukončování víceúčastnických multimediálních konferenčních hovorů.

## Popis

Conference Call Device (CCD) je základní aplikační server v architektuře IMS, standardizovaný v 3GPP TS 23.153. Funguje jako centrální řadič pro multimediální konferenční relace a zajišťuje jak signalizační, tak mediální aspekty. CCD komunikuje s dalšími základními prvky IMS, jako je Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), přičemž pro řízení relace používá [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol). Přijímá SIP INVITE požadavky na vytvoření konference nebo přidání účastníka, autentizuje a autorizuje uživatele na základě předplatitelských dat a řídí navázání mediálních spojení mezi všemi účastníky konference.

Z architektonického hlediska se CCD skládá z několika logických komponent: funkce řízení konferenční politiky (Conference Policy Control Function), konferenčního centra (Conference Focus) a schopností zpracování médií (Media Processing). Konferenční centrum je centrální SIP uživatelský agent, který udržuje stav dialogu s každým účastníkem a spravuje seznam účastníků konference. Funkce řízení konferenční politiky vynucuje pravidla týkající se toho, kdo se může připojit, zvát další nebo manipulovat s konferencí (např. ztlumení). Pro zpracování médií může CCD buď fungovat jako mediální mixér (Media Mixer), který kombinuje audio/video proudy od všech účastníků do jednoho složeného proudu odesílaného každému z nich, nebo jako mediální přeposílač/řadič (Media Relay/Controller), který instruuje koncové body, aby odesílaly média do vyhrazeného procesoru funkce mediálních zdrojů ([MRFP](/mobilnisite/slovnik/mrfp/)) pro mixování.

Jeho provoz zahrnuje několik klíčových procedur. Pro vytvoření ad-hoc konference uživatel zahájí základní hovor a poté použije SIP REFER nebo jiné mechanismy, aby instruoval CCD k přidání dalších stran. Pro naplánované konference CCD jedná na základě předem zřízených dat. Během konference CCD zpracovává události v průběhu hovoru, jako je připojení/odpojení účastníka, renegociace médií a sběr [DTMF](/mobilnisite/slovnik/dtmf/) tónů pro ovládání v rámci konference (např. 'stiskněte 1 pro ztlumení'). Poskytuje také informace pro účtování systémům offline a online účtování ([OCS](/mobilnisite/slovnik/ocs/), [OFCS](/mobilnisite/slovnik/ofcs/)) pro účely fakturace. Role CCD je klíčová pro zajištění plynulého, nízkolatenčního a funkčně bohatého konferenčního zážitku, který abstrahuje složitost od koncových uživatelských zařízení.

## K čemu slouží

CCD bylo zavedeno za účelem standardizace a umožnění bohatých, operátorské úrovně (carrier-grade) konferenčních služeb v rámci vznikajícího rámce IP Multimedia Subsystem (IMS) definovaného ve 3GPP Release 5. Před IMS byly víceúčastnické hlasové hovory možné v přepojovaných sítích (např. pomocí služby Multi-Party Service v GSM), ty však byly funkčně omezené, těsně svázané s hlasem a obtížně integrovatelné s nově vznikajícími IP multimediálními službami. Motivací bylo vytvořit flexibilní, škálovatelnou a na síť orientovanou konferenční platformu, která by podporovala hlasové, video a datové relace a umožnila operátorům nové výnosové služby.

Řeší problém fragmentovaných proprietárních konferenčních řešení tím, že poskytuje standardizovanou referenční architekturu a postupy. To zajišťuje interoperabilitu mezi zařízeními od různých výrobců a napříč různými síťovými operátory, což uživatelům umožňuje konzistentní zážitek. Model CCD centralizuje složitou řídicí logiku konference v síti, čímž snižuje nároky na schopnosti uživatelského zařízení. To umožňuje i jednoduchým telefonům účastnit se pokročilých konferencí, protože inteligence je umístěna v síťovém CCD. Navíc tím, že je CCD součástí jádra IMS, může využívat mechanismy IMS pro autentizaci, zabezpečení, autorizaci QoS a integrované účtování, čímž poskytuje bezpečnou a účtovatelnou službu.

Vytvoření CCD bylo hnací silou přechodu odvětví na plně IP sítě a snahy nabízet rozšířené komunikační služby nad rámec základních hlasových hovorů. Řešilo omezení peer-to-peer konferenčních modelů, které byly obtížně škálovatelné, říditelné a zpeněžitelné. Definováním CCD poskytlo 3GPP základ pro širokou škálu komerčních a podnikových konferenčních služeb, od jednoduchých třístranných hovorů po rozsáhlé naplánované webináře s nahráváním médií a řízením přístupu k řečnickému právu.

## Klíčové vlastnosti

- Centralizované řízení založené na SIP pro zřizování a správu víceúčastnických multimediálních relací
- Podpora jak ad-hoc (okamžitých), tak předem připravených (naplánovaných) typů konferencí
- Integrované schopnosti zpracování médií, fungující jako mixér nebo řídící externí MRFP
- Vynucování politiky pro přijetí účastníka, jeho oprávnění a akce v rámci konference
- Generování podrobných záznamů o účtovaných datech (CDR) pro fakturaci konferenčních služeb
- Spolupracuje s legacy konferenčními službami v přepojovaných sítích pro konvergenci sítí

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRFP – Multimedia Resource Function Processor](/mobilnisite/slovnik/mrfp/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2

---

📖 **Anglický originál a plná specifikace:** [CCD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccd/)

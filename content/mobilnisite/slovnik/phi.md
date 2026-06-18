---
slug: "phi"
url: "/mobilnisite/slovnik/phi/"
type: "slovnik"
title: "PHI – Packet Handler Interface"
date: 2025-01-01
abbr: "PHI"
fullName: "Packet Handler Interface"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/phi/"
summary: "Interní rozhraní uvnitř paketově orientované jádrové sítě UMTS (PS-CN), konkrétně mezi SGSN a GGSN. Standardizuje komunikaci pro funkce zpracování a směrování paketů a zajišťuje tak interoperabilitu m"
---

PHI je standardizované rozhraní mezi SGSN a GGSN v jádrové síti UMTS, které umožňuje komunikaci pro zpracování a směrování paketů za účelem interoperability mezi zařízeními různých výrobců.

## Popis

Rozhraní pro obsluhu paketů (Packet Handler Interface, PHI) je standardizované interní rozhraní definované ve specifikacích 3GPP pro architekturu paketového jádra UMTS (Universal Mobile Telecommunications System). Působí mezi uzly [SGSN](/mobilnisite/slovnik/sgsn/) (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node) a GGSN (Gateway GPRS Support Node), což jsou dva hlavní uzly pro zpracování paketových dat v síťové architektuře 3GPP Release 99 a Release 4/5. PHI není protokol uživatelské ani řídicí roviny vystavený externím sítím; jde spíše o interní abstrakci, která definuje logické funkce a výměnu dat potřebnou pro zpracování paketů, směrování a tunelování mezi těmito jádrovými síťovými prvky. Zahrnuje mechanismy pro vytváření a správu tunelů [GTP](/mobilnisite/slovnik/gtp/) (GPRS Tunneling Protocol), obsluhu kontextů [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol) a přenos paketů uživatelských dat.

Architektonicky PHI představuje funkční hranici a soubor primitiv, která umožňují SGSN a GGSN bezproblémově spolupracovat. SGSN, které je zodpovědné za správu mobility a relací směrem k rádiové přístupové síti, používá PHI k předávání uživatelských dat příslušnému GGSN, jež slouží jako brána k externím paketovým datovým sítím, jako je internet. Rozhraní zajišťuje správné zapouzdření paketů do GTP tunelů, jejich směrování na základě PDP kontextu účastníka a uplatňování profilů kvality služeb (QoS). Mezi klíčové součásti fungování PHI patří správa identifikátorů koncových bodů tunelů ([TEID](/mobilnisite/slovnik/teid/)), zpracování informací pro účtování a podpora scénářů roamování mezi různými [PLMN](/mobilnisite/slovnik/plmn/).

V praxi specifikace PHI (3GPP TS 21.905) poskytuje podrobný popis služeb a funkcí, které musí být na tomto logickém rozhraní podporovány, aby byla zaručena interoperabilita mezi výrobci. Zatímco podkladovým protokolem pro tuto komunikaci je GTP ([GTP-C](/mobilnisite/slovnik/gtp-c/) pro řídicí rovinu a [GTP-U](/mobilnisite/slovnik/gtp-u/) pro uživatelská data), PHI definuje požadavky a chování na vyšší vrstvě. Jeho role byla zásadní pro paketové jádro UMTS, neboť umožnilo jasné oddělení odpovědností: SGSN se stará o mobilitu na straně rádia a správu přenosových kanálů, zatímco GGSN spravuje externí konektivitu a přidělování IP adres. Tato modularita byla klíčová pro škálování raných 3G sítí a podporu rozmanitého ekosystému výrobců síťového vybavení.

## K čemu slouží

PHI bylo vytvořeno, aby vyřešilo kritickou potřebu standardizace a interoperability v rodící se paketově orientované jádrové síti 3G. Před jeho definicí mohla proprietární rozhraní mezi síťovými uzly vést k závislosti na jednom dodavateli, což zvyšovalo náklady a složitost pro mobilní operátory nasazující sítě UMTS. PHI poskytlo jasné, standardizované logické rozhraní mezi SGSN a GGSN, které zajišťovalo, že zařízení od různých výrobců mohou bezproblémově spolupracovat. To byl základní požadavek pro úspěšné komerční zavádění 3G datových služeb, neboť podpořilo konkurenční prostředí s více dodavateli a urychlilo nasazování sítí.

Historicky byl vývoj PHI součástí širšího úsilí 3GPP vyvinout sítě GSM směrem k paketovým datovým schopnostem s GPRS a EDGE, které vyvrcholilo plnou architekturou UMTS. Vyřešilo problém, jak čistě oddělit uzel obsluhy s povědomím o mobilitě (SGSN) od funkce IP brány (GGSN), a zároveň stanovit robustní a interoperabilní komunikační metodu mezi nimi. Rozhraní standardizovalo zpracování paketů uživatelských dat, správu tunelů a související řídicí procedury, které byly dříve předmětem implementačně specifických variací. Definováním PHI zajistilo 3GPP konzistentní architektonický plán, který podporoval spolehlivé směrování paketů, účtování a správu QoS ve všech kompatibilních síťových nasazeních.

Motivace vycházela z omezení dřívějších, více monolitických síťových návrhů a z potřeby vytvořit flexibilní, škálovatelné jádro sítě schopné podporovat vysokorychlostní přístup k internetu a nově vznikající mobilní datové aplikace. PHI jako součást celkových specifikací jádra GPRS/UMTS umožnilo přechod od okruhově orientovaných hlasových sítí k integrovaným paketově orientovaným architekturám, které jsou základem moderního mobilního broadbandu. Položilo základy pro později vyvinuté paketové jádro (EPC) v 4G LTE, které tyto koncepty dále abstrahovalo a vylepšovalo.

## Klíčové vlastnosti

- Standardizuje logickou komunikaci mezi SGSN a GGSN
- Definuje primitiva pro vytváření a správu GTP tunelů
- Podporuje obsluhu a směrování kontextů PDP (Packet Data Protocol)
- Zajišťuje interoperabilitu mezi síťovými prvky od různých výrobců
- Umožňuje přenos a zapouzdření uživatelských dat uvnitř jádra sítě
- Poskytuje rámec pro výměnu informací pro účtování

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [PHI na 3GPP Explorer](https://3gpp-explorer.com/glossary/phi/)

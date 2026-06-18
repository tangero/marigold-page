---
slug: "j2se"
url: "/mobilnisite/slovnik/j2se/"
type: "slovnik"
title: "J2SE – Java 2 Platform, Standard Edition"
date: 2025-01-01
abbr: "J2SE"
fullName: "Java 2 Platform, Standard Edition"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/j2se/"
summary: "J2SE je základní platforma Java pro desktopová a serverová prostředí. Ve standardu 3GPP je zmíněna v rámci architektury Open Service Access (OSA), kde jsou aplikační servery hostující aplikace síťovýc"
---

J2SE je základní platforma Java pro vývoj a provoz aplikačních serverů, které hostují síťové služby v rámci architektury Open Service Access (OSA) standardu 3GPP.

## Popis

Java 2 Platform, Standard Edition (J2SE), později známá jako Java [SE](/mobilnisite/slovnik/se/), je hlavní vývojová a běhová platforma Java pro všeobecné výpočetní účely. V architektuře 3GPP je její hlavní význam jako základní technologie pro implementaci architektury Open Service Access ([OSA](/mobilnisite/slovnik/osa/)), jak je podrobně popsáno ve specifikacích jako TS 23.057. OSA je klíčovou součástí servisní vrstvy 3GPP, navrženou pro umožnění bezpečného a standardizovaného přístupu k síťovým schopnostem (jako je řízení hovorů, lokalizace uživatele nebo zasílání zpráv) poskytovatelům aplikací třetích stran. Samotné aplikační programové rozhraní ([API](/mobilnisite/slovnik/api/)) OSA je definováno pomocí Unified Modeling Language ([UML](/mobilnisite/slovnik/uml/)) a je mapováno na konkrétní technologické vazby, přičemž vazba pro Java je nejvýznamnější a nejrozšířenější.

Architektura zahrnuje bránu OSA (také nazývanou Parlay Gateway), která funguje jako bezpečný prostředník mezi jádrovou sítí a externími aplikačními servery. Tato brána i aplikační servery, které se k ní připojují, jsou typicky implementovány pomocí platforem J2SE (a její podnikové varianty J2EE). Brána zpřístupňuje síťové funkce prostřednictvím sady rozhraní Java známých jako Service Capability Features ([SCF](/mobilnisite/slovnik/scf/)), například Generic Call Control nebo User Location. Externí aplikační server, napsaný v Javě a běžící v prostředí J2SE/J2EE, používá tato klientská Java API k vyhledání, vyjednání přístupu a volání těchto síťových služeb. Komunikace mezi aplikačním serverem a bránou OSA často používá [CORBA](/mobilnisite/slovnik/corba/) nebo, v pozdějších implementacích, webové služby, ale programovací model pro vývojáře aplikací je čistá Java.

Funguje to tak, že poskytovatel služeb vyvíjí aplikaci v Javě, která využívá klientské knihovny OSA. Tato aplikace běží na standardním aplikačním serveru J2SE/J2EE. Naváže zabezpečené spojení s bránou OSA, ověří se a poté může začít vytvářet servisní relace. Například může vytvořit instanci objektu pro řízení hovoru k uskutečnění hlasového hovoru mezi dvěma stranami, přičemž brána OSA převádí tato volání metod v Javě na příslušné signalizační zprávy (např. [SIP](/mobilnisite/slovnik/sip/), [MAP](/mobilnisite/slovnik/map/)) směrem k jádrové síti. Platforma J2SE poskytuje robustní, škálovatelné a bezpečné běhové prostředí nezbytné pro tyto komponenty serverů úrovně operátora. Její role tedy není technologie uvnitř mobilního zařízení (jako J2ME), ale umožňující technologie pro servisní infrastrukturu na síťové straně, která otevírá telekomunikační síť podnikovým inovacím a inovacím třetích stran.

## K čemu slouží

Účelem odkazování na J2SE ve standardu 3GPP bylo využít zralou, široce přijímanou a platformně nezávislou technologii pro stavbu kritických serverových komponent architektury Open Service Access (OSA). Před OSA byl přístup třetích stran k síťovým schopnostem zajišťován prostřednictvím proprietárních rozhraní specifických pro dodavatele, což vedlo k závislosti na dodavateli, vysokým integračním nákladům a zpomalení tvorby nových služeb. Iniciativa OSA si kladla za cíl vytvořit standardizované, na dodavateli nezávislé API.

Volba Javy/J2SE jako primární implementační technologie pro toto API řešila několik klíčových problémů. Za prvé poskytla vysokou úroveň, objektově orientovaný programovací model, který byl známý velkému množství podnikových vývojářů, což jim usnadnilo vytváření telekomunikačních aplikací bez nutnosti hlubokých znalostí signalizačních protokolů. Za druhé, filozopie Javy „napiš jednou, spusť kdekoliv“ dokonale odpovídala cíli přenositelnosti aplikací mezi různými implementacemi brány OSA od různých síťových dodavatelů. Servisní aplikace napsaná pro Java OSA API by teoreticky měla fungovat s jakoukoli kompatibilní bránou. Nakonec, J2SE a J2EE nabízely komplexní sadu vestavěných funkcí pro zabezpečení, správu transakcí a škálovatelnost, které byly nezbytné pro vytváření spolehlivých servisních platforem úrovně operátora. To umožnilo průmyslu soustředit se na standardizaci rozhraní servisní logiky namísto základní middleware vrstvy, což urychlilo přijetí otevřenosti sítě.

## Klíčové vlastnosti

- Primární implementační platforma pro bránu a aplikace služeb 3GPP OSA/Parlay
- Poskytuje technologickou vazbu Java pro standardizovaná OSA API
- Umožňuje vývoj přenositelných telekomunikačních aplikací nezávislých na konkrétní síti
- Využívá robustní funkce Javy pro zabezpečení a škálovatelnost pro servery úrovně operátora
- Usnadňuje jasné oddělení funkcí jádra sítě a servisní logiky
- Slouží jako běhové prostředí pro klienty a servery Service Capability Feature (SCF)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [J2SE na 3GPP Explorer](https://3gpp-explorer.com/glossary/j2se/)

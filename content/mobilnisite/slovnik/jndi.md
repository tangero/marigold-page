---
slug: "jndi"
url: "/mobilnisite/slovnik/jndi/"
type: "slovnik"
title: "JNDI – Java Naming and Directory Interface"
date: 2025-01-01
abbr: "JNDI"
fullName: "Java Naming and Directory Interface"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/jndi/"
summary: "Java API poskytující aplikacím pojmenovací a adresářové funkce, které jim umožňují prostřednictvím jména objevovat a vyhledávat data a objekty. V kontextech 3GPP se na něj odkazuje u rozhraní pro sprá"
---

JNDI je Java API poskytující pojmenovací a adresářové funkce, které umožňuje aplikacím a komponentám 3GPP sítí standardizovaným způsobem prostřednictvím jména objevovat a vyhledávat distribuované prostředky.

## Popis

Java Naming and Directory Interface (JNDI) je Java [API](/mobilnisite/slovnik/api/) specifikované společností Oracle (dříve Sun Microsystems), které poskytuje jednotné rozhraní pro přístup k různým pojmenovacím a adresářovým službám. Abstrahuje detaily různých implementací adresářových služeb, jako jsou [LDAP](/mobilnisite/slovnik/ldap/), [DNS](/mobilnisite/slovnik/dns/) nebo NIS, a umožňuje tak aplikacím v Javě provádět operace jako lookup, bind, unbind a rebind konzistentním způsobem. JNDI funguje prostřednictvím architektury service provider interface ([SPI](/mobilnisite/slovnik/spi/)), kde poskytovatelé implementují API pro konkrétní adresářové služby, což aplikacím umožňuje komunikovat s různými backendovými systémy bez změny kódu.

V architektuře sítí 3GPP není JNDI základním telekomunikačním protokolem, ale je zmíněno ve specifikacích pro manažerská a servisně orientovaná rozhraní. Lze jej použít v systémech pro správu sítí ([NMS](/mobilnisite/slovnik/nms/)), servisních platformách nebo operačních podpůrných systémech ([OSS](/mobilnisite/slovnik/oss/)), kde aplikace založené na Javě potřebují objevovat a přistupovat k distribuovaným prostředkům, jako jsou konfigurační data, uživatelské profily nebo koncové body služeb. Například v servisně orientované architektuře ([SOA](/mobilnisite/slovnik/soa/)) pro telekomunikační služby může JNDI usnadňovat vyhledávání komponent Enterprise JavaBeans (EJB) nebo jiných komponent nasazených napříč servery.

API se skládá z klíčových komponent, jako je rozhraní Context, které reprezentuje sadu vazeb jméno-objekt, a rozhraní DirContext, které jej rozšiřuje pro adresářové služby s atributy. Aplikace pro navázání spojení s pojmenovací nebo adresářovou službou využívají počáteční továrnu kontextů (initial context factory) a specifikují vlastnosti jako [URL](/mobilnisite/slovnik/url/) poskytovatele a bezpečnostní přihlašovací údaje. JNDI podporuje synchronní i asynchronní operace, ačkoli jeho použití v telekomunikační signalizaci v reálném čase je omezené kvůli všeobecnému zaměření Javy a potenciální latenci.

Přestože samotné JNDI není technologií definovanou 3GPP, jeho zařazení do specifikací 3GPP (např. 21.905 pro slovník a 23.057 pro aspekty služeb) naznačuje jeho roli v standardizovaných rozhraních pro správu služeb nebo aplikační rámce. Umožňuje interoperabilitu ve vícevýrobních prostředích tím, že poskytuje společný mechanismus pro zjišťování prostředků, což může zjednodušit integraci síťových aplikací založených na Javě s adresářovými službami, jako jsou ty používané pro data účastníků nebo správu politik.

## K čemu slouží

JNDI bylo vytvořeno pro řešení fragmentace v pojmenovacích a adresářových službách napříč různými systémy a protokoly. Před jeho zavedením musely aplikace v Javě používat proprietární nebo službě specifická API pro komunikaci s adresáři jako LDAP nebo DNS, což vedlo ke složitému nepřenositelnému kódu. JNDI poskytuje jediné standardizované API, které tyto rozdíly abstrahuje, a podporuje tak opětovné využití kódu a snazší údržbu v distribuovaných výpočetních prostředích.

V kontextu sítí 3GPP odkaz na JNDI ve specifikacích podporuje potřebu škálovatelného zjišťování a správy služeb. Jak se telekomunikační sítě vyvíjely směrem k více softwarově řízeným a servisně orientovaným architekturám, zejména s přijetím Javy v manažerských platformách, nabídlo JNDI způsob, jak dynamicky lokalizovat a navazovat vazby na síťové prostředky. To je obzvláště užitečné v operačních podpůrných systémech (OSS) nebo obchodních podpůrných systémech (BSS), kde komponenty potřebují přistupovat ke sdíleným adresářům pro konfiguraci nebo data účastníků.

Motivace pro zahrnutí JNDI do dokumentace 3GPP vychází z jeho rozšířeného použití v podnikových ekosystémech Javy, které se překrývají s telekomunikačními manažerskými řešeními. Pomáhá řešit problémy spojené s vyhledáváním prostředků v distribuovaných nasazeních, jako je nalezení koncových bodů služeb nebo uživatelských profilů, bez nutnosti pevného zakódování jejich umístění. Nicméně nenahrazuje základní telekomunikační protokoly jako Diameter nebo HTTP/2; místo toho je doplňuje v manažerských a aplikačních vrstvách, což umožňuje flexibilnější a udržitelnější síťový software.

## Klíčové vlastnosti

- Jednotné API pro více pojmenovacích a adresářových služeb (např. LDAP, DNS, NIS)
- Rozhraní poskytovatele služeb (SPI) pro rozšiřitelnost o nové typy adresářů
- Podpora operací s kontextem, jako je lookup, bind, unbind a rebind
- Integrace s podnikovými technologiemi Javy jako EJBs a JMS
- Zásuvné (pluggable) bezpečnostní kontexty pro ověřený přístup k adresářům
- Mechanismy pro notifikaci událostí při změnách v adresářových datech

## Související pojmy

- [LDAP – Lightweight Directory Access Protocol](/mobilnisite/slovnik/ldap/)
- [DNS – Directory Name Service](/mobilnisite/slovnik/dns/)
- [SOA – Suppress Outgoing Access (CUG SS)](/mobilnisite/slovnik/soa/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [JNDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/jndi/)

---
slug: "j2me"
url: "/mobilnisite/slovnik/j2me/"
type: "slovnik"
title: "J2ME – Java 2 Platform, Micro Edition"
date: 2025-01-01
abbr: "J2ME"
fullName: "Java 2 Platform, Micro Edition"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/j2me/"
summary: "J2ME je platforma Java navržená pro zařízení s omezenými prostředky, jako jsou starší feature telefony a vestavěné systémy. Poskytovala standardizované prostředí pro vývoj a nasazení přenositelných ap"
---

J2ME je platforma Java navržená pro zařízení s omezenými prostředky, jako jsou starší mobilní telefony, která poskytuje standardizované prostředí pro vývoj přenositelných aplikací a umožňuje stahovatelné služby před érou smartphonů.

## Popis

Java 2 Platform, Micro Edition (J2ME), později známá jako Java [ME](/mobilnisite/slovnik/me/), je redukovaná verze programovacího jazyka Java a běhového prostředí specificky optimalizovaná pro zařízení s omezenou pamětí, výpočetním výkonem a možnostmi zobrazení. V kontextu 3GPP je standardizována jako součást architektur Open Service Access ([OSA](/mobilnisite/slovnik/osa/)) a Mobile Station Application Execution Environment (MExE), primárně specifikovaných v TS 23.057. J2ME poskytuje vrstvu abstrahující hardware, což vývojářům umožňuje psát aplikace (zvané MIDlets), které mohou běžet na jakémkoli kompatibilním zařízení bez úprav pro podkladový čipset nebo operační systém.

Architektura J2ME pro mobilní zařízení je založena na konfiguracích a profilech. Connected Limited Device Configuration ([CLDC](/mobilnisite/slovnik/cldc/)) je základní soubor Java [API](/mobilnisite/slovnik/api/) a funkcí virtuálního stroje pro zařízení s velmi omezenými prostředky (jako starší mobilní telefony). Nad tím přidává Mobile Information Device Profile ([MIDP](/mobilnisite/slovnik/midp/)) API pro uživatelské rozhraní, trvalé ukládání a síťovou konektivitu. Mobilní telefon s podporou J2ME obsahuje kompaktní Java Virtual Machine ([KVM](/mobilnisite/slovnik/kvm/) - Kilobyte Virtual Machine) implementující CLDC spolu s knihovnami MIDP. Aplikace jsou baleny jako MIDlet sady (soubory JAR s přidruženým deskriptorovým souborem [JAD](/mobilnisite/slovnik/jad/)), které lze stáhnout přes vzdušné rozhraní ([OTA](/mobilnisite/slovnik/ota/)) nebo jinými prostředky. Architektura MExE, jak ji definuje 3GPP, klasifikuje J2ME jako 'MExE classmark', což umožňuje síti identifikovat schopnosti zařízení pro provádění aplikací za účelem vyjednávání služeb a zabezpečení.

Jak J2ME funguje: platforma MExE v zařízení spravuje životní cyklus MIDlets. Když uživatel vybere J2ME aplikaci, Application Management Software (AMS) platformy ověří MIDlet sadu, zkontroluje digitální podpisy, pokud jsou vyžadovány, nainstaluje ji a poté vytvoří instanci a řídí MIDlet (spustí, pozastaví, ukončí). MIDlet komunikuje s nativními funkcemi zařízení (obrazovka, klávesnice, síť) prostřednictvím standardizovaných MIDP API. Pro síťovou konektivitu typicky používá Generic Connection Framework (GCF), který může navazovat HTTP nebo jiná spojení, což umožňuje aplikacím komunikovat se servery. To umožnulo širokou škálu služeb, od jednoduchých her a osobních organizérů po klienty pro e-mail, počasí a zprávy. Jeho role v raných sítích 3GPP byla jako hlavní technologie umožňující stahovatelné přidané služby, což vytvořilo ekosystém aplikací třetích stran před nástupem moderních platformových operačních systémů pro smartphony jako iOS a Android.

## K čemu slouží

J2ME bylo vytvořeno, aby řešilo problém fragmentovaných proprietárních platforem na raném trhu mobilních telefonů. Před jeho přijetím byly mobilní aplikace typicky psány v nativním kódu pro specifické rodiny čipsetů zařízení, což je činilo nepřenositelnými a nákladnými na vývoj pro různé typy zařízení. Tato fragmentace brzdila inovace a rozvoj širokého trhu mobilního softwaru. Účelem standardizace J2ME v rámci 3GPP (prostřednictvím MExE) bylo definovat univerzální, bezpečné aplikační prostředí, které by mohlo být nasazeno na široké škále mobilních terminálů od různých výrobců.

Řešilo klíčový problém přenositelnosti služeb a dostupnosti pro vývojáře. Síťoví operátoři a poskytovatelé služeb mohli vyvinout službu jednou a nasadit ji milionům účastníků bez ohledu na model jejich telefonu, pokud podporoval požadovaný profil J2ME. To dramaticky snížilo vstupní bariéru pro poskytovatele mobilního obsahu a aplikací. Dále standardizace 3GPP MExE integrovala J2ME do servisní architektury sítě, což umožnilo funkce jako objevování služeb a bezpečná autentizace. Byla to klíčová technologie pro realizaci vize 3G jako platformy pro datové služby nad rámec jednoduchého hlasu a SMS, což umožnilo první vlnu interaktivního mobilního obsahu a připravilo cestu pro dnešní ekonomiku aplikací.

## Klíčové vlastnosti

- Standardizované běhové prostředí Java pro zařízení s omezenými prostředky (CLDC/MIDP)
- Umožňuje přenositelný vývoj aplikací prostřednictvím API abstrahujících hardware
- Podporuje poskytování a instalaci MIDlet sad přes vzdušné rozhraní (OTA)
- Integrováno do architektury MExE 3GPP pro rozpoznání schopností zařízení
- Poskytuje zabezpečený sandbox pro provádění aplikací s řízeným přístupem k prostředkům zařízení
- Umožňuje síťovou konektivitu pro aplikace prostřednictvím Generic Connection Framework (GCF)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [J2ME na 3GPP Explorer](https://3gpp-explorer.com/glossary/j2me/)

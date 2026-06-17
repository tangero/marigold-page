---
slug: "af-as"
url: "/mobilnisite/slovnik/af-as/"
type: "slovnik"
title: "AF/AS – Application Function / Application Server"
date: 2025-01-01
abbr: "AF/AS"
fullName: "Application Function / Application Server"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/af-as/"
summary: "AF/AS je síťová funkce, která poskytuje služby specifické pro aplikace a komunikuje s jádrem sítě 5G (5G Core), aby ovlivňovala směrování provozu a rozhodnutí o politikách. Umožňuje aplikacím třetích"
---

AF/AS je síťová funkce, která poskytuje služby specifické pro aplikace a komunikuje s jádrem sítě, aby ovlivňovala směrování provozu a rozhodnutí o politikách, což umožňuje integraci aplikací třetích stran.

## Popis

Application Function ([AF](/mobilnisite/slovnik/af/)) / Application Server ([AS](/mobilnisite/slovnik/as/)) je klíčová architektonická komponenta v architektuře založené na službách (Service-Based Architecture, SBA) podle 3GPP, zejména od sítě 5G. Představuje entitu, která hostuje aplikační logiku a vyžaduje interakci s jádrem sítě 5G (5G Core, 5GC) pro podporu svých služeb. AF/AS není součástí jádra sítě definovaného 3GPP, ale je důvěryhodnou externí entitou, která komunikuje s funkcemi jádra sítě, především s funkcí pro vystavení sítě (Network Exposure Function, [NEF](/mobilnisite/slovnik/nef/)) a funkcí pro řízení politik (Policy Control Function, [PCF](/mobilnisite/slovnik/pcf/)), prostřednictvím standardizovaných rozhraní založených na službách.

Z architektonického hlediska je AF/AS propojena s jádrem 5G přes NEF, která funguje jako zabezpečená brána a abstrakční vrstva. NEF řízeným způsobem vystavuje schopnosti a události sítě 3GPP pro AF, a zároveň agreguje a překládá požadavky AF pro interní síťové funkce. Pro přímou, důvěryhodnou komunikaci (v rámci domény operátora) může AF komunikovat také přímo s PCF. Jako hlavní protokoly se používají [HTTP](/mobilnisite/slovnik/http/)/2 s datovými částmi ve formátu [JSON](/mobilnisite/slovnik/json/), v souladu s principy rozhraní založených na službách 3GPP definovaných v řadě specifikací TS 29.500.

Jak to funguje, zahrnuje několik klíčových interakcí. AF může poskytovat PCF informace týkající se sezení, jako je požadovaná šířka pásma, latence nebo rozkmit pro konkrétní aplikační tok. To umožňuje PCF vytvářet odpovídající pravidla pro řízení politik a účtování (Policy and Charging Control, PCC). AF se může také prostřednictvím NEF přihlásit k odběru síťových událostí (např. změna polohy UE, ztráta připojení). Když k takové události dojde, NEF o tom AF informuje, což umožňuje aplikaci dynamicky reagovat. Dále může AF ovlivňovat směrování provozu žádostí o konkrétní názvy datových sítí (Data Network Names, [DNN](/mobilnisite/slovnik/dnn/)) nebo výběr síťového řezu (network slice), což umožňuje připojení s ohledem na aplikaci.

Její role sahá až k umožnění síťových schopností pro vertikální odvětví a poskytovatele služeb třetích stran. Prostřednictvím rozhraní AF/AS mohou aplikace žádat o služby s garantovaným přenosovým tokem pro kritické komunikace, spouštět síťově iniciované servisní požadavky pro zařízení IoT nebo přistupovat k analytickým informacím. AF/AS je ústřední pro vizi 5G o programovatelnosti a vystavení sítě, která transformuje síť z pouhého kanálu pro připojení na programovatelnou platformu, kterou lze přizpůsobit různorodým potřebám aplikací, od vylepšeného mobilního širokopásmového připojení až po ultra-spolehlivou komunikaci s nízkou latencí a masové IoT.

## K čemu slouží

Koncept [AF](/mobilnisite/slovnik/af/)/AS byl vytvořen, aby překlenul propast mezi službami aplikační vrstvy a základními schopnostmi mobilní sítě. Historicky aplikace běžely 'přes vrchol' s omezenou viditelností nebo kontrolou nad síťovými podmínkami. To vedlo k podoptimálnímu uživatelskému zážitku, protože aplikace se nemohly přizpůsobit zahlcení sítě, latenci nebo událostem mobility. AF/AS poskytuje standardizovaný, zabezpečený mechanismus, kterým aplikace mohou komunikovat své požadavky a přijímat síťové informace, což umožňuje optimalizované poskytování služeb.

Klíčový problém, který řeší, je statická povaha tradičního řízení kvality služeb (QoS) a politik. Dříve byly síťové politiky z velké části definovány operátorem a byly obecné. AF/AS umožňuje dynamické řízení politik řízené aplikací. Například služba cloudového hraní může požádat o tok s nízkou latencí a vysokou šířkou pásma pro uživatelské sezení pouze tehdy, když je hra aktivní, čímž zlepšuje efektivitu využití zdrojů. Řeší také potřebu vystavení sítě pro podporu inovací, což umožňuje vývojářům třetích stran vytvářet aplikace s povědomím o síti, aniž by potřebovali hluboké znalosti vnitřních mechanismů 3GPP.

Motivace vychází z různorodých požadavků případů užití 5G. Vertikální odvětví, jako je automobilový průmysl, zdravotnictví a průmyslové IoT, vyžadují specifické chování sítě (např. garantovanou latenci, vysokou spolehlivost), které nelze uspokojit univerzální sítí. AF/AS spolu s řezy sítě (network slicing) a řízením politik poskytuje rozhraní, pomocí kterého mohou tato vertikální odvětví 'komunikovat' se sítí a zajistit, aby byly splněny jejich smlouvy o úrovni služeb. Transformuje síť z uzavřeného systému na otevřenou platformu podporující rozsáhlý ekosystém inovativních služeb.

## Klíčové vlastnosti

- Dynamické řízení politik ovlivněné aplikací prostřednictvím interakce s PCF
- Přihlášení k odběru a oznamování síťových událostí (např. mobilita UE, stav připojení) prostřednictvím NEF
- Ovlivnění směrování provozu a výběru síťového řezu pro aplikační sezení
- Zabezpečené vystavení síťových schopností důvěryhodným externím aplikacím
- Podpora kvality služeb (QoS) s ohledem na aplikaci, včetně garantovaného přenosového toku a cílů pro latenci
- Umožňuje síťově iniciované servisní požadavky pro efektivní komunikaci zařízení IoT

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [AF/AS na 3GPP Explorer](https://3gpp-explorer.com/glossary/af-as/)

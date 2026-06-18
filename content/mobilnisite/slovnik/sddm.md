---
slug: "sddm"
url: "/mobilnisite/slovnik/sddm/"
type: "slovnik"
title: "SDDM – SEAL Data Delivery Management"
date: 2025-01-01
abbr: "SDDM"
fullName: "SEAL Data Delivery Management"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sddm/"
summary: "SDDM je servisní rámec 3GPP pro správu doručování dat v ekosystému SEAL (Service Enabler Architecture Layer). Poskytuje standardizované mechanismy pro distribuci dat, odběr a notifikace, což umožňuje"
---

SDDM je servisní rámec 3GPP v ekosystému SEAL, který poskytuje standardizované mechanismy pro správu doručování dat, včetně distribuce, odběru a notifikací, aby umožnil efektivní komunikaci mezi službami.

## Popis

[SEAL](/mobilnisite/slovnik/seal/) Data Delivery Management (SDDM) je klíčový funkční rámec definovaný v rámci architektury Service Enabler Architecture Layer (SEAL) od 3GPP. Jeho primární role spočívá v orchestrování spolehlivého a efektivního doručování dat mezi různými službami (service enablers) a klientskými aplikacemi. Architektonicky SDDM funguje jako schopnost servisní vrstvy, typicky hostovaná v doméně síťového operátora nebo v důvěryhodném prostředí třetí strany. Abstrahuje složitosti přímé distribuce dat a poskytuje standardizované rozhraní založené na [API](/mobilnisite/slovnik/api/), které umožňuje producentům dat publikovat informace a konzumentům dat odebírat relevantní datové proudy. Rámec spravuje životní cyklus relací doručování dat, zpracovává autorizaci odběrů a zajišťuje směrování dat na správné koncové body na základě definovaných politik a profilů odběratelů.

V jádru SDDM funguje implementací modelu publikování a odběru (publish-subscribe, pub/sub). Služby (service enablers) fungující jako zdroje dat (servery [SDDM-S](/mobilnisite/slovnik/sddm-s/)) registrují své dostupné datové sady v rámci SDDM. Klientské aplikace nebo jiné služby (klienti [SDDM-C](/mobilnisite/slovnik/sddm-c/)) si pak mohou tyto zdroje dat vyhledat a přihlásit se k jejich odběru. Systém SDDM spravuje tyto odběry, včetně ověření vůči uživatelským profilům a síťovým politikám. Když zdroj publikuje nová data, SDDM je zodpovědný za určení seznamu autorizovaných odběratelů a zahájení procesu doručení. Toto doručení může být založené na push (notifikace odeslané okamžitě) nebo na pull (data načtená klientem), v závislosti na požadavcích služby a schopnostech klienta.

Klíčovými komponentami architektury SDDM jsou SDDM klient (SDDM-C), SDDM server (SDDM-S) a SDDM Management Function. SDDM-C je entita, která konzumuje data, iniciuje žádosti o odběr a zpracovává přijatá data nebo notifikace. SDDM-S je entita, která produkuje a publikuje data, čímž je zpřístupňuje k odběru. SDDM Management Function, potenciálně distribuovaná, zajišťuje centrální koordinaci, včetně správy odběrů, směrování, vynucování politik a potenciálně zprostředkování mezi více klienty a servery. Její role v síti spočívá v usnadnění oddělené, škálovatelné a efektivní servisní vrstvy, kde je aplikační logika oddělena od podkladových mechanismů distribuce dat, což urychluje vývoj a nasazení nových vertikálních služeb.

## K čemu slouží

SDDM byl vytvořen, aby řešil rostoucí potřebu standardizovaného, nativně síťového rámce pro distribuci dat mezi službami (service enablers) v sítích 5G a budoucích sítích. Před jeho zavedením služby na servisní vrstvě často spoléhaly na proprietární nebo nestandardizované integrace typu point-to-point pro sdílení dat, což vedlo ke složitým integracím, závislosti na dodavateli a neefektivnímu využívání síťových zdrojů. Rozmach internetu věcí (IoT), edge computingu a síťových expozičních [API](/mobilnisite/slovnik/api/) zvýraznil omezení těchto ad-hoc přístupů, zejména pro scénáře doručování dat v reálném čase řízené politikami.

Primární problém, který SDDM řeší, je absence jednotného mechanismu pro doručování dat mezi službami v ekosystému 3GPP. Umožňuje čisté oddělení mezi servisní logikou („co“) a mechanismy doručování dat („jak“). To umožňuje vývojářům služeb soustředit se na funkčnost aplikace a spoléhat na síť, která zajišťuje spolehlivou, bezpečnou a efektivní distribuci dat. Je motivován vizí architektury [SEAL](/mobilnisite/slovnik/seal/), která si klade za cíl poskytnout společnou sadu znovupoužitelných služeb (jako je správa skupin, správa konfigurace a doručování dat), aby urychlila vytváření vertikálních aplikací pro oblasti jako [V2X](/mobilnisite/slovnik/v2x/), průmyslový IoT a veřejná bezpečnost.

Historicky byly podobné schopnosti buď vestavěny do monolitických servisních platforem, nebo implementovány pomocí obecných webových technologií bez povědomí o síti. Vytvoření SDDM v rámci standardů 3GPP zajišťuje jeho optimalizaci pro telekomunikační prostředí s vestavěnou podporou pro síťové identity (jako [SUPI](/mobilnisite/slovnik/supi/)), QoS politiky, události mobility a integraci s dalšími funkcemi jádra sítě 3GPP. To poskytuje úroveň spolehlivosti, zabezpečení a kontextového povědomí, kterou externí řešení typu over-the-top nemohou snadno dosáhnout.

## Klíčové vlastnosti

- Standardizovaný model distribuce dat typu publikování a odběru (publish-subscribe, pub/sub)
- Oddělená architektura rozdělující producenty dat (SDDM-S) a konzumenty dat (SDDM-C)
- Podpora jak notifikací založených na push, tak načítání dat založeného na pull
- Integrace s 3GPP autentizací, autorizací a profily odběratelů
- Řízení směrování a spouštění doručování dat na základě politik
- Mechanismus pro vyhledávání dostupných zdrojů dat klienty

## Související pojmy

- [SEAL – Service Enabler Architecture Layer for Verticals](/mobilnisite/slovnik/seal/)
- [SDDM-C – SEAL Data Delivery Management Client](/mobilnisite/slovnik/sddm-c/)
- [SDDM-S – SEAL Data Delivery Management Server](/mobilnisite/slovnik/sddm-s/)
- [CAPIF – Common API Framework](/mobilnisite/slovnik/capif/)

## Definující specifikace

- **TS 24.538** (Rel-19) — MSGin5G Service Protocol Specification
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol

---

📖 **Anglický originál a plná specifikace:** [SDDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/sddm/)

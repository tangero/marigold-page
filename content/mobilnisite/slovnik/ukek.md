---
slug: "ukek"
url: "/mobilnisite/slovnik/ukek/"
type: "slovnik"
title: "UKEK – Unique Key Encryption Key (P25)"
date: 2026-01-01
abbr: "UKEK"
fullName: "Unique Key Encryption Key (P25)"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ukek/"
summary: "Kryptografický klíč používaný ve službách 3GPP Proximity Services (ProSe) pro veřejnou bezpečnost. Šifruje klíč ProSe Group Key, čímž chrání skupinovou komunikaci pro služby kritické z hlediska mise,"
---

UKEK je kryptografický klíč používaný ve službách 3GPP Proximity Services, který šifruje klíč ProSe Group Key za účelem ochrany zabezpečené skupinové komunikace pro veřejnou bezpečnost.

## Popis

Unique Key Encryption Key (UKEK) je bezpečnostní klíč definovaný v architektuře 3GPP pro služby založené na blízkosti ([ProSe](/mobilnisite/slovnik/prose/)), konkrétně pro aplikace veřejné bezpečnosti. Jeho primární funkcí je šifrovat jiný klíč, ProSe Group Key ([PGK](/mobilnisite/slovnik/pgk/)), který se používá k zabezpečení skupinové komunikace (např. push-to-talk hlas, data) mezi uživatelskými zařízeními (UE) ve scénáři přímého objevování a komunikace ProSe. UKEK je odvozen funkcí ProSe v síti, konkrétně pro danou aplikaci ProSe a konkrétní UE. Tvoří klíčovou součást hierarchie klíčů pro zabezpečení skupinové komunikace ProSe.

Z architektonického hlediska je UKEK generován a spravován funkcí ProSe v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)). Proces začíná, když UE, vystupující jako vlastník skupiny ProSe, požádá o autorizaci pro skupinovou komunikaci. Funkce ProSe žádost ověří a v případě schválení odvodí UKEK. K tomuto odvození se typicky používá kód aplikace ProSe, identita UE a kořenový klíč sdílený mezi UE a sítí. UKEK je následně použit k zašifrování klíče ProSe Group Key (PGK) před jeho odesláním žadajícímu UE přes zabezpečený kanál. UE, disponující potřebnými přihlašovacími údaji, může UKEK a následně i PGK dešifrovat.

Během provozu je zašifrovaný PGK (obalený UKEK) distribuován členům skupiny. Každé UE člena použije svůj vlastní jedinečný UKEK k dešifrování PGK. Po dešifrování je společný PGK použit k odvození klíčů pro šifrování provozu, které zabezpečují vlastní média a signalizaci relace skupinové komunikace přes referenční bod PC5 (přímé rozhraní zařízení-zařízení). Tato dvouvrstvá hierarchie klíčů (UKEK chrání PGK, PGK chrání provoz) poskytuje jak zabezpečení, tak škálovatelnost. Zajišťuje, že i pokud je skupinový klíč pro jednoho uživatele kompromitován, přímo to neohrozí skupinovou komunikaci ostatních členů, protože jejich verze chráněné UKEK zůstávají bezpečné. Tento mechanismus je zásadní pro zajištění důvěrnosti a integrity komunikací kritických z hlediska mise, používaných personálem veřejné bezpečnosti, které probíhají mimo síť.

## K čemu slouží

UKEK byl zaveden, aby řešil konkrétní bezpečnostní výzvy ve službách 3GPP Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) pro veřejnou bezpečnost, standardizovaných zejména od Release 13 a dále vylepšovaných v pozdějších vydáních. Jádrem problému je zabezpečení skupinové komunikace, když zařízení komunikují přímo (Device-to-Device, [D2D](/mobilnisite/slovnik/d2d/)) bez neustálého spoléhání se na síťovou infrastrukturu, což je běžné v katastrofických scénářích, kdy mohou být základnové stanice poškozeny. Tradiční zabezpečení v celulárních sítích spoléhá na klíče ukotvené v síťovém jádru, které není v přímém režimu vždy dostupné.

Motivace pro vytvoření UKEK pramení z potřeby bezpečného, efektivního a řiditelného mechanismu distribuce klíčů pro skupinovou komunikaci. Bez něj by bylo obtížné bezpečně distribuovat společný skupinový klíč mnoha zařízením. Jednoduchý přístup zasílání stejného klíče všem členům je nezabezpečený. UKEK tento problém řeší tím, že pro každého člena poskytuje jedinečný obal. Umožňuje síťové funkci ProSe distribuovat jednu zašifrovanou verzi skupinového klíče ([PGK](/mobilnisite/slovnik/pgk/)), kterou může dešifrovat pouze zamýšlené přijímající UE pomocí svého jedinečného UKEK. Tím se řeší omezení starších nebo nestandardizovaných D2D systémů, které často měly slabší, méně škálovatelné bezpečnostní modely.

Historicky bylo jeho specifikace v Release 15 (a souvisejících specifikacích) součástí procesu dozrávání rámců ProSe a Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)). Umožňuje zabezpečenou službu Mission Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) v síťovém i mimosíťovém (přímém) režimu, což je základním požadavkem pro složky veřejné bezpečnosti přijímající LTE a 5G. UKEK zajišťuje, že robustní, standardizované zabezpečení sítí 3GPP se spolehlivě rozšiřuje do náročných prostředí přímé komunikace používaných složkami IZS.

## Klíčové vlastnosti

- Jedinečný klíč pro každé UE, používaný k šifrování klíče ProSe Group Key (PGK)
- Odvozen síťovou funkcí ProSe pomocí přihlašovacích údajů specifických pro UE
- Umožňuje bezpečnou distribuci skupinových klíčů pro přímou komunikaci ProSe
- Součást dvouvrstvé hierarchie klíčů pro zvýšené zabezpečení skupinové komunikace
- Zásadní pro zabezpečení služeb kritických z hlediska mise (MCS), jako je push-to-talk v mimosíťovém režimu
- Chrání důvěrnost skupinové komunikace přes rozhraní PC5

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [PGK – ProSe Group Key](/mobilnisite/slovnik/pgk/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems

---

📖 **Anglický originál a plná specifikace:** [UKEK na 3GPP Explorer](https://3gpp-explorer.com/glossary/ukek/)

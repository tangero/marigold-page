---
slug: "ptm-m"
url: "/mobilnisite/slovnik/ptm-m/"
type: "slovnik"
title: "PTM-M – Point to Multipoint – Multicast"
date: 2025-01-01
abbr: "PTM-M"
fullName: "Point to Multipoint – Multicast"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ptm-m/"
summary: "PTM-M je režim PTM služby pro multicastové doručování, při kterém je obsah odesílán specifické skupině účastníků, kteří o něj projevili zájem. Je základním mechanismem pro předplatné služby jako kanál"
---

PTM-M je režim služby point-to-multipoint (bod–více bodů) pro multicastové doručování, který odesílá obsah specifické skupině účastníků, kteří o něj projevili zájem, což umožňuje efektivní distribuci pro služby jako mobilní TV.

## Popis

Point to Multipoint – Multicast (PTM-M) označuje multicastový režim [PTM](/mobilnisite/slovnik/ptm/) služeb, při kterém jsou data doručována z jednoho zdroje specifické skupině uživatelů, kteří si službu aktivně předplatili nebo se k ní připojili. Na rozdíl od broadcastu, který cílí na všechny uživatele v oblasti, PTM-M cílí pouze na autorizované příjemce, což jej činí vhodným pro služby založené na předplatném nebo prémiový obsah. Tento režim je základní součástí architektury [MBMS](/mobilnisite/slovnik/mbms/).

Technický provoz zahrnuje několik fází. Nejprve se uživatelé přihlásí k odběru multicastové služby, často prostřednictvím mechanismu oznámení služby. Když je služba aktivní, síť vytvoří multicastový přenosový kontext. V páteřní síti se [BM-SC](/mobilnisite/slovnik/bm-sc/) stará o správu předplatného, distribuci klíčů pro šifrování služby (pro placený obsah) a iniciaci relace směrem k RAN. V rádiové síti jsou multicastová data naplánována na sdílený kanál (např. [MTCH](/mobilnisite/slovnik/mtch/) v LTE/NR). Data vysílají pouze buňky, ve kterých jsou aktivní přihlášení uživatelé, čímž se šetří rádiové prostředky. Mezi klíčové protokoly patří MBMS-specifický [GTP](/mobilnisite/slovnik/gtp/) pro uživatelskou rovinu a signalizace řídicí roviny pro spuštění/ukončení relace a správu členství.

Úlohou PTM-M je umožnit efektivní a škálovatelné doručování obsahu, jako je živé [TV](/mobilnisite/slovnik/tv/), rádio, stahování souborů nebo aktualizace softwaru, velké, ale definované skupině příjemců. Optimalizuje síťové prostředky tím, že data přenáší jednou přes sdílené spoje a replikuje je co nejpozději v topologii sítě. Tento režim je zásadní pro komerční distribuci obsahu, protože umožňuje účtování specifické pro službu, správu digitálních práv a garantovanou kvalitu služeb pro předplatitele.

## K čemu slouží

PTM-M byl vytvořen, aby řešil potřebu střední cesty mezi neefektivním unicastem a nerozlišujícím broadcastem. Čistý broadcast plýtvá prostředky vysíláním do oblastí bez zainteresovaných uživatelů, zatímco unicast k mnoha uživatelům není škálovatelný. PTM-M řeší problém efektivního doručování obsahu velké, geograficky rozptýlené skupině uživatelů, kteří se k odběru přihlásili, jako jsou předplatitelé balíčku mobilní [TV](/mobilnisite/slovnik/tv/).

Historický kontext je spojen s vývojem [MBMS](/mobilnisite/slovnik/mbms/), kdy poskytovatelé služeb hledali způsob, jak nabízet prémiové multimediální služby ziskově. PTM-M umožňuje správu předplatného, ochranu obsahu prostřednictvím šifrování a cílené doručování, což jsou nezbytné prvky životaschopného obchodního modelu. Řeší tak omezení starších metod distribuce obsahu, kterým tyto podrobné kontroly chyběly.

PTM-M dále podporuje aplikace jako bezdrátové aktualizace softwaru pro zařízení IoT nebo správu vozových parků, kde je třeba aktualizace odeslat konkrétní sadě zařízení. Jeho účelem je poskytnout síťově efektivní, bezpečnou a řiditelnou metodu pro distribuci obsahu typu jeden–více, kde je členství v publiku známé a kontrolované, což usnadňuje nové služby a zdroje příjmů pro operátory.

## Klíčové vlastnosti

- Doručování obsahu pouze přihlášeným/připojeným uživatelům (selektivní multicast)
- Integrovaná správa předplatného a autorizace služby
- Podpora zabezpečeného doručování obsahu prostřednictvím správy služebních klíčů MBMS
- Efektivní využití rádiových prostředků na základě přítomnosti aktivních uživatelů v buňkách
- Schopnost doručování metodami streamování i stahování souborů
- Mechanismy účtování založené na předplatném služby nebo její spotřebě

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [PTM-M na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptm-m/)
